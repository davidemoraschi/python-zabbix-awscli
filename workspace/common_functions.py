#!/usr/bin/python
'''
Common function module:
1. execute_S3_sql_files_in_Athena() - scans a folder to find SQL files and executes them on Athena
2. log_environment() - Logs passed arguments to CloudWatch
3. get_args() - Extracts environment from sys.argv
'''

import platform
import sys
import time
import logging
from typing import Dict
import boto3
import awswrangler as wr
from tabulate import tabulate
from config import AWS_REGION, AWS_BUCKET, AWS_FOLDER, AWS_ATHENA_DATABASE, AWS_ATHENA_OUPUT, AWS_PROFILE

LOG_DELAY = 50/1000


def execute_s3_sql_files_athena(logger, environment):
    '''Reads files from S3'''

    if environment == 'vscode':
        vscode_session = boto3.Session(
            region_name=AWS_REGION, profile_name=AWS_PROFILE)
        s3_client = vscode_session.client(service_name='s3')
    else:
        glue_session = boto3.Session()
        s3_client = glue_session.client('s3')

    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(AWS_BUCKET)
    logger.info('AWS_BUCKET: \n%s', AWS_BUCKET)
    logger.info('AWS_FOLDER: \n%s', AWS_FOLDER)
    for sqlfile in s3_bucket.objects.filter(Prefix=AWS_FOLDER):
        if sqlfile.key.endswith('sql'):
            s3_file = s3_client.get_object(Bucket=AWS_BUCKET, Key=sqlfile.key)
            querystring = (s3_file['Body'].read().decode('utf-8'))

            # --if environment == 'sandbox':
            time.sleep(LOG_DELAY)
            logger.info('Running Query: \n%s', querystring)

            df = wr.athena.read_sql_query(sql=querystring, database=AWS_ATHENA_DATABASE, ctas_approach=False, s3_output=AWS_ATHENA_OUPUT)
            logger.info(f'Filename: {sqlfile.key:90} - Returned rows: {df.shape[0]:4}')
            if df.shape[0] > 0:
                logger.info('\n' + tabulate(df, headers=df.keys(), tablefmt='psql', showindex=False))


def log_environment(logger, environment, job_name, job_run_id, args):
    '''Logs variables for the job'''

    if environment != 'vscode':
        logger.info('Arguments              : %s', args)
        time.sleep(LOG_DELAY)
        logger.info('Environment            : %s', environment)
        time.sleep(LOG_DELAY)
        logger.info('Platform               : %s', platform.platform())
        time.sleep(LOG_DELAY)
        logger.info('Python                 : %s', platform.python_version())
        time.sleep(LOG_DELAY)
        logger.info('PYTHONPATH             : %s', sys.path)
        time.sleep(LOG_DELAY)
        logger.info('boto3                  : %s', boto3.__version__)
        time.sleep(LOG_DELAY)
        logger.info('awswrangler            : %s', wr.__version__)
        time.sleep(LOG_DELAY)
        logger.info('JOB_SCRIPT             : %s', str(sys.argv[0]))
        time.sleep(LOG_DELAY)
        logger.info('JOB_NAME               : %s', job_name)
        time.sleep(LOG_DELAY)
        logger.info('JOB_RUN_ID             : %s', job_run_id)
        time.sleep(LOG_DELAY)
        logger.info('AWS_REGION             : %s', AWS_REGION)
        time.sleep(LOG_DELAY)
        logger.info('AWS_BUCKET             : %s', AWS_BUCKET)
        time.sleep(LOG_DELAY)
        logger.info('AWS_ATHENA_DATABASE    : %s', AWS_ATHENA_DATABASE)
        time.sleep(LOG_DELAY)


def get_args(args):
    '''Reads arguments from command line'''
    env_value = ''
    for i in range(1, len(args)):
        if args[i].find("--bucket_name") == 0:
            env_value = args[i+1]
            break
    return env_value


class InfoDebugFilter(logging.Filter):
    '''I don't know what to write here, it's just a class that I copied from somewhere.'''

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
