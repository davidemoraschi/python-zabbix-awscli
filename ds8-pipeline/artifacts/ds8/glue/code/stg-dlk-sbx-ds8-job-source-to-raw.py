#!/usr/bin/python
'''
Python Shell jobs on AWS Glue:
1. Connects to SFTP server from a Glue job - Stored secret contains the credentials and host/port of SFTP server
2. Downloads gzip file, uncompress it, extract JSON node and recompress it (Must run with 1DPU because of memory error with 1/16DPU)
3. Uploads to S3 bucket for further processing and deletes original file
davide.moraschi@toptal.com 2024
'''

import time
import boto3
import jq
import json
from tabulate import tabulate
from gzip_s3_and_json_py3 import download_json_gz, upload_json_gz, get_newest_file_from_sftp
from common_functions import log, log_environment, process_arguments, send_sns
from config import AWS_REGION, AWS_SECRET_NAME, FTP_FOLDER, FTP_FILE_PATTERN, S3_BUCKET, S3_PATH
from typing import Dict, List

# Process command line arguments
args: Dict[str, str] = process_arguments(options=['WORKFLOW_NAME', 'WORKFLOW_RUN_ID'])

# Print arguments for debugging
print(tabulate(tabular_data=args.items(), headers=['args.keys()', 'args.values()'], tablefmt='psql', showindex=False))

# Parse workflow name, job name from arguments
WORKFLOW_NAME: str = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID: str = args['WORKFLOW_RUN_ID']
JOB_NAME: str = args['JOB_NAME'] if 'JOB_NAME' in args else 'stg-dlk-sbx-ds8-job-source-to-raw'
JOB_RUN_ID: int = int(time.time())

def main():
    '''Guess what, I'm the main module...'''

    # Log environment information for debugging
    log_environment()

    # Log start of job
    log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
        job_run_id=str(JOB_RUN_ID), str_message='start-job', bigint_rows_retrieved=0, float_latest_epoch=JOB_RUN_ID*1000)

    s3client = boto3.client('s3')
    ftp_filename = get_newest_file_from_sftp(AWS_REGION, AWS_SECRET_NAME, FTP_FOLDER, FTP_FILE_PATTERN, s3client, S3_BUCKET, S3_PATH)
    products_feed = download_json_gz(s3client, S3_BUCKET, S3_PATH + ftp_filename)
    # glue_job_logger.info('Extracting products node from JSON')
    products = jq.compile(".products[] as $parent | $parent.localizedAttributes.en_XD.name as $productname | $parent | {code, brand, $productname, salesAreaProperties}").input_value(
        products_feed).text()
    s3_filename = ftp_filename.replace('_compressed.gz', '')
    upload_json_gz(glue_job_logger, s3client, S3_BUCKET, S3_PATH + '{0}.gz'.format(s3_filename), products)
    response = s3client.delete_object(Bucket=S3_BUCKET, Key=S3_PATH + ftp_filename)

    # Mark the end of the Job execution for Monitoring with CloudWatch.
    glue_job_logger.info('JOB_NAME.JOB_RUN_ID           : %s.%s | end-job', JOB_NAME, str(JOB_RUN_ID))


if __name__ == "__main__":
    main()
