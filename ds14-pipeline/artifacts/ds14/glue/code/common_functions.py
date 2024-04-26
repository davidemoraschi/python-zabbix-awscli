#!/usr/bin/python
'''
Common function module:
1. execute_S3_sql_files_in_Athena() - scans a folder to find SQL files and executes them on Athena
2. log_environment() - Logs passed arguments to CloudWatch
3. get_args() - Extracts environment from sys.argv
'''

import platform
import sys
import logging.config
import logging
import time
from typing import Dict, Any
from functools import lru_cache
from config import AWS_REGION, AWS_BUCKET, AWS_ATHENA_DATABASE, AWS_ATHENA_OUPUT, AWS_ATHENA_LOG_TABLE, S3_BUCKET, SQL_QUERIES_BUCKET, SQL_QUERIES_FOLDER, S3_PATH, SNS_FAILURE_TOPIC  # pylint: disable=line-too-long
import boto3
import awswrangler as wr
from tabulate import tabulate
from awsglue.utils import getResolvedOptions  # type: ignore # pylint: disable=import-error

def process_arguments(options) -> Dict[str, str]:
    '''These parameters will be populated by the trigger job paramters in Workflow or default to the Job configuration parameters'''

    args: dict[str, str] = getResolvedOptions(args=sys.argv, options=options)
    return args

LOG_DELAY = 50/1000

# Process command line arguments
args: Dict[str, str] = process_arguments(options=['WORKFLOW_NAME', 'WORKFLOW_RUN_ID', 'environment'])

# Print arguments for debugging
print(tabulate(tabular_data=args.items(), headers=['args.keys()', 'args.values()'], tablefmt='psql', showindex=False))

# Parse report IDs, workflow name, EVENT_TYPES, and job name from arguments
WORKFLOW_NAME: str = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID: str = args['WORKFLOW_RUN_ID']
ENVIRONMENT: str = args['environment']
JOB_NAME: str = args['JOB_NAME'] if 'JOB_NAME' in args else f'stg-dlk-{ENVIRONMENT}-ds6-job-raw-to-refined'
JOB_RUN_ID: int = int(time.time())

aws_bucket = AWS_BUCKET.replace('${var.env}',ENVIRONMENT)
aws_athena_database = AWS_ATHENA_DATABASE.replace('${var.env}',ENVIRONMENT)
s3_bucket = S3_BUCKET.replace('${var.env}',ENVIRONMENT)
s3_path = S3_PATH.replace('${var.env}',ENVIRONMENT)
sql_queries_bucket = SQL_QUERIES_BUCKET.replace('${var.env}',ENVIRONMENT)
aws_athena_output = AWS_ATHENA_OUPUT.replace('${var.env}',ENVIRONMENT)

class InfoDebugFilter(logging.Filter):  # pylint: disable=too-few-public-methods
    '''Class InfoDebugFilter.'''

    def filter(self, record):
        """Filter debug and info messages."""
        return record.levelno in (logging.DEBUG, logging.INFO)


def default_logging_config(level: str = "INFO", formatter_name: str = "detailed") -> Dict:
    """
    Create default logging config.

    Parameters
    ----------
    level
        Log level.
    formatter_name
        Log formatter name. Possible values: detailed or dev.

    Returns
    -------
        Dictionary compatible with logging.config.dictConfig.

    """
    logging_config = {
        "version": 1,
        "filters": {"info_debug_filter": {"()": InfoDebugFilter}},
        "formatters": {
            "detailed": {
                "class": "logging.Formatter",
                "format": "%(asctime)s %(levelname)-8s %(name)-15s - %(message)s",
            },
            "dev": {
                "class": "logging.Formatter",
                "format": "%(asctime)s %(levelname)s %(name)s - ++++++++ %(message)s ++++++++",
            },
        },
        "handlers": {
            "debug_handler": {
                "class": "logging.StreamHandler",
                "formatter": formatter_name,
                "level": "DEBUG",
                "filters": ["info_debug_filter"],
                "stream": "ext://sys.stdout",
            },
            "warning": {
                "class": "logging.StreamHandler",
                "formatter": formatter_name,
                "level": "WARNING",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "job": {
                "level": level,
                "propagate": False,
                "handlers": ["debug_handler", "warning"],
            },
            "glue_shared": {
                "level": level,
                "propagate": False,
                "handlers": ["debug_handler", "warning"],
            },
        },
        "root": {"level": "WARNING", "handlers": ["debug_handler", "warning"]},
    }

    return logging_config

logging.config.dictConfig(config=default_logging_config(level='DEBUG'))
glue_job_logger: logging.Logger = logging.getLogger(name='job')

def create_etl_log_table(n:int=0) -> None:
    '''Creates the Athena _etl_log table'''

    database_name: str = aws_athena_database
    sql_query: str = f'''CREATE TABLE IF NOT EXISTS "{aws_athena_database}".{AWS_ATHENA_LOG_TABLE}
                            WITH (table_type = 'ICEBERG',
                                format = 'ORC', 
                                write_compression ='ZSTD',
                                location = 's3://stg-dlk-{ENVIRONMENT}-ds-{n}-raw/iceberg/_etl_log/', 
                                is_external = false,
                            --      partitioning = ARRAY['month(dt)'],
                                vacuum_min_snapshots_to_keep = 10,
                                vacuum_max_snapshot_age_seconds = 604800
                            ) 
                            AS 
                            SELECT 
                                to_unixtime(current_timestamp)*1000 AS double_epoch_ts_log
                                ,'ds{n}-pipeline' AS str_glue_workflow_name
                                ,'0' AS str_glue_workflow_runid
                                ,'stg-dlk-{ENVIRONMENT}-ds{n}-job-source-to-raw' AS str_glue_job_name
                                ,0 AS int_glue_job_runid
                                ,'auditLog' AS str_glue_job_step
                                ,CAST(123456789 AS BIGINT) AS bigint_rows_retrieved
                                ,CAST('' AS VARCHAR(2000)) AS str_error_message
                            WHERE 1=0;
                        '''

    get_query_execution: dict = wr.athena.start_query_execution(sql=sql_query,
                                                                database=database_name,
                                                                wait=True)

    print(f'{get_query_execution["Status"]["State"]} in {get_query_execution["Statistics"]["TotalExecutionTimeInMillis"]}ms')


def log(workflow_name: str = WORKFLOW_NAME, workflow_run_id: str = WORKFLOW_RUN_ID, job_name: str = JOB_NAME,
        job_run_id: str = str(JOB_RUN_ID), str_message: str = '', bigint_rows_retrieved: int = 0,
        float_latest_epoch: float = 0, str_error_message: str = '') -> None:
    '''Writes to the job log file and to the Athena _etl_log table'''

    time.sleep(LOG_DELAY)
    float_latest_epoch = int(1000*float(time.time()))

    glue_job_logger.info(msg=f'WORKFLOW_NAME.WORKFLOW_RUN_ID|JOB_NAME.JOB_RUN_ID: {workflow_name}.{workflow_run_id}|{job_name}.{job_run_id}|{str_message}')

    database_name: str = aws_athena_database
    sql_query: str = f'''INSERT INTO "{aws_athena_database}".{AWS_ATHENA_LOG_TABLE}(double_epoch_ts_log,str_glue_workflow_name,str_glue_workflow_runid,
                            str_glue_job_name,int_glue_job_runid,str_glue_job_step,bigint_rows_retrieved,str_error_message) 
                        VALUES(:float_latest_epoch;,:str_glue_workflow_name;,:str_glue_workflow_runid;,
                            :str_glue_job_name;,:int_glue_job_runid;,:str_glue_job_step;,:bigint_rows_retrieved;,:str_error_message;)'''

    get_query_execution: dict = wr.athena.start_query_execution(sql=sql_query,
                                                                database=database_name,
                                                                params={
                                                                    "float_latest_epoch": float_latest_epoch,
                                                                    "str_glue_workflow_name": f"'{workflow_name}'",
                                                                    "str_glue_workflow_runid": f"'{workflow_run_id}'",
                                                                    "str_glue_job_name": f"'{job_name}'",
                                                                    "int_glue_job_runid": job_run_id,
                                                                    "str_glue_job_step": f"'{str_message}'",
                                                                    "bigint_rows_retrieved": bigint_rows_retrieved,
                                                                    "str_error_message": f"'{str_error_message}'"
                                                                },
                                                                wait=True)

    print(f'{get_query_execution["Status"]["State"]} in {get_query_execution["Statistics"]["TotalExecutionTimeInMillis"]}ms')


def get_last_loaded_epoch() -> float:
    '''Returns the last loaded epoch from the Athena _etl_log table'''

    database_name: str = AWS_ATHENA_DATABASE
    sql_query: str = f'''SELECT MAX(double_epoch_ts_log) AS last_loaded_epoch FROM {AWS_ATHENA_LOG_TABLE}'''

    df = wr.athena.read_sql_query(sql=sql_query, database=database_name, ctas_approach=False, s3_output=aws_athena_output)

    # print(df)
    return float(df['last_loaded_epoch'][0])


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    '''Returns the nth fibonacci number'''

    fib: list[int] = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


def execute_s3_sql_files_athena(workflow_name: str = WORKFLOW_NAME, workflow_run_id: str = WORKFLOW_RUN_ID,
                                job_name: str = JOB_NAME, job_run_id: str = str(JOB_RUN_ID)):
    '''Reads files from S3'''

    glue_session = boto3.Session()
    s3_client = glue_session.client('s3')

    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(sql_queries_bucket)

    # Logs sql_queries_bucket.SQL_QUERIES_FOLDER
    log(workflow_name=workflow_name, workflow_run_id=workflow_run_id, job_name=job_name,
        job_run_id=str(job_run_id), str_message=f'SQL_QUERIES_BUCKET/SQL_QUERIES_FOLDER: {sql_queries_bucket}/{SQL_QUERIES_FOLDER}')

    for sqlfile in s3_bucket.objects.filter(Prefix=SQL_QUERIES_FOLDER):
        if sqlfile.key.endswith('sql'):
            s3_file = s3_client.get_object(Bucket=sql_queries_bucket, Key=sqlfile.key)
            querystring = (s3_file['Body'].read().decode('utf-8')).replace('${var.env}',ENVIRONMENT)
            print(querystring)

            log(workflow_name=workflow_name, workflow_run_id=workflow_run_id, job_name=job_name,
                job_run_id=str(job_run_id), str_message=querystring.partition('\n')[0])
            
            df = wr.athena.read_sql_query(sql=querystring, database=aws_athena_database, ctas_approach=False, s3_output=aws_athena_output)

            log(workflow_name=workflow_name, workflow_run_id=workflow_run_id, job_name=job_name,
                job_run_id=str(job_run_id), str_message=f'Filename: {sqlfile.key}', bigint_rows_retrieved=df.shape[0])

            if df.shape[0] > 0:
                log(workflow_name=workflow_name, workflow_run_id=workflow_run_id, job_name=job_name,
                    job_run_id=str(job_run_id), str_message='\n' + tabulate(df, headers=df.keys(), tablefmt='psql', showindex=False))


def log_environment():
    '''Logs variables for the job'''

    env_dict = {}
    env_dict["Platform"] = platform.platform()
    env_dict["Python"] = platform.python_version()
    # env_dict["PYTHONPATH"]              = sys.path
    env_dict["boto3"] = boto3.__version__
    env_dict["awswrangler"] = wr.__version__
    env_dict["AWS_REGION"] = AWS_REGION
    env_dict["AWS_BUCKET"] = aws_bucket
    env_dict["AWS_ATHENA_DATABASE"] = aws_athena_database
    env_dict["S3_BUCKET"] = s3_bucket
    env_dict["S3_PATH"] = s3_path

    time.sleep(LOG_DELAY)
    print(tabulate(env_dict.items(), headers=['variable', 'value'], tablefmt='psql', showindex=False))
    time.sleep(LOG_DELAY)
    print(f'PYTHONPATH: {sys.path}')
    return JOB_RUN_ID, ENVIRONMENT


def get_args(args):
    '''Reads arguments from command line'''
    env_value = ''
    for i in range(1, len(args)):
        if args[i].find("--bucket_name") == 0:
            env_value = args[i+1]
            break
    return env_value


def send_sns(workflow_name: str = WORKFLOW_NAME, workflow_run_id: str = WORKFLOW_RUN_ID,
             job_name: str = JOB_NAME, job_run_id: str = str(JOB_RUN_ID), exc: Any = '') -> None:
    '''Sends an SNS message to the failure topic'''

    sns = boto3.client('sns')
    response = sns.publish(TopicArn=SNS_FAILURE_TOPIC,
                           Message=f'WORKFLOW_NAME={workflow_name}\nWORKFLOW_RUN_ID={workflow_run_id}\nJOB_NAME={job_name}\nJOB_RUN_ID={job_run_id}\n{str(exc)}')
    print(response)


if __name__ == '__main__':
    pass
