#!/usr/bin/python
'''
# Python Shell jobs on AWS Glue:
# 1. Does a POST API call to create a token
# 2. Uses the token to authenticate to another API and start creating an export file
# 3. Checks for execution and when done downloads the CSV result
# davide.moraschi@toptal.com 2024
'''

import io
import sys
import logging.config
import logging
import json
import time
import zipfile
import boto3
import requests
from tabulate import tabulate
from awsglue.utils import getResolvedOptions
from common_functions import default_logging_config, log_environment
from gzip_s3_and_json_py3 import get_secret_credentials, upload_json_gz
from config import AWS_REGION, AWS_SECRET_NAME, S3_BUCKET, S3_PATH
from TokenManager import TokenManager

def process_arguments():
    '''These parameters will be populated by the trigger job paramters in Workflow or default to the Job configuration parameters'''

    args = getResolvedOptions(sys.argv, ['WORKFLOW_NAME', 'WORKFLOW_RUN_ID', 'REPORT_IDS'])
    return args

def fibonacci(n):
    '''Returns the nth fibonacci number'''
    
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def retrieve_access_token():
    '''Retrieves the access token from AWS Secrets Manager'''

    try:
        credentials = get_secret_credentials(AWS_REGION, AWS_SECRET_NAME)
        token_url = 'https://clearcorrect.docebosaas.com/oauth2/token'
        refresh_token = None  
        token_manager = TokenManager(token_url, credentials, refresh_token)
        access_token = token_manager.get_token()
        return access_token
    except Exception as exc:
        raise

def create_export_report_csv(REPORT_ID):
    '''Calls the Docebo API to start a report extraction'''

    try:
        token = retrieve_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/export/csv'
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()                                         # Raise an exception for bad status codes
        execution_id = response.json()['data']['executionId']
        return execution_id
    except Exception as exc:
        raise

def download_export_report_csv(REPORT_ID, execution_id):
    '''Calls the Docebo API to download the report zip file'''

    try:
        token = retrieve_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        is_completed = False
        fibonacci_index = 1
        url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/exports/{execution_id}'

        while not is_completed:
            sleep_time = fibonacci(fibonacci_index)                         # Get the Fibonacci number
            fibonacci_index += 1                                            # Increment Fibonacci index for the next iteration
            time.sleep(sleep_time)                                          # Sleep for the Fibonacci number of seconds
            print(sleep_time)
            response = requests.get(url=url, headers=headers)               # Calls the endpoint to get report status
            response.raise_for_status()                                     # Raise an exception for bad status codes
            is_completed = (response.json()['data']['status']=='SUCCEEDED') # Check if finished

        url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/exports/{execution_id}/download'
        response = requests.get(url=url, headers=headers)                   # Calls the endpoint to download report zip file
        response.raise_for_status()                                         # Raise an exception for bad status codes
        with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref: # Unzips the content on the fly
            zip_ref.extractall('./')                                        # Saves into current folder
            return zip_ref.filelist
    except Exception as exc:
        raise

args = process_arguments()
logging.config.dictConfig(default_logging_config(level='DEBUG'))
glue_job_logger = logging.getLogger(name='job')
print(tabulate(args.items(), headers=['args.keys()','args.values()'], tablefmt='psql', showindex=False))

REPORT_IDS          = json.loads(args['REPORT_IDS'])
WORKFLOW_NAME       = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID     = args['WORKFLOW_RUN_ID']
JOB_NAME            = args['JOB_NAME'] if 'JOB_NAME' in args else 'stg-dlk-sbx-ds6-job-source-to-raw'
JOB_RUN_ID          = int(time.time())
LOG_DELAY           = 50/1000

def log(str_message):
    '''Writes to the jopb log file'''

    time.sleep(LOG_DELAY)
    glue_job_logger.info(f'WORKFLOW_NAME.WORKFLOW_RUN_ID|JOB_NAME.JOB_RUN_ID: {WORKFLOW_NAME}.{WORKFLOW_RUN_ID}|{JOB_NAME}.{JOB_RUN_ID}|{str_message}')

def main():
    '''Guess what, I'm the main module...'''
    
    try:
        # Prints to log several useful info for debugging purposes.
        log_environment()        
        log('start-job')

        for report_id in REPORT_IDS:

            # Logs the current report
            log(f'Running report_id:{report_id}')

            # Runs the report and creates the csv
            execution_id = create_export_report_csv(report_id)

            # Downloads the zipped CSV
            filelist = download_export_report_csv(report_id, execution_id)

            # Uploads to the raw bucket
            s3client = boto3.client('s3')
            for csvfile in filelist:
                s3_filename = csvfile.filename
                with open(s3_filename, 'r') as file:
                    csvcontent = file.read()
                upload_json_gz(glue_job_logger, s3client, S3_BUCKET, S3_PATH + f'{str(JOB_RUN_ID)}-{s3_filename}.gz', csvcontent)

        # Mark the end of the Job execution for Monitoring with CloudWatch.
        log('end-job')

    except Exception as exc:
        log(f'An error occurred:{str(exc)}')
        log('end-job')
        raise

if __name__ == "__main__":
    main()
