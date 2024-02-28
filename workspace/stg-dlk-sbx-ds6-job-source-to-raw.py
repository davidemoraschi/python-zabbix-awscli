#!/usr/bin/python
'''
# Python Shell jobs on AWS Glue:
# 1. Does a POST API call to create a token
# 2. Uses the token to authenticate to another API and start creating an export file
# 3. Checks for execution and when done downloads the CSV result
# davide.moraschi@toptal.com 2024
'''

import io
import logging.config
import logging
import sys
import time
import zipfile
import requests
import boto3
from awsglue.utils import getResolvedOptions
from gzip_s3_and_json_py3 import get_secret_credentials, upload_json_gz
from common_functions import default_logging_config
from config import AWS_REGION, AWS_SECRET_NAME, S3_BUCKET, S3_PATH
from TokenManager import TokenManager

logging.config.dictConfig(default_logging_config(level='DEBUG'))
glue_job_logger = logging.getLogger(name='job')

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def retrieve_access_token():
    credentials = get_secret_credentials(AWS_REGION, AWS_SECRET_NAME)
    token_url = 'https://clearcorrect.docebosaas.com/oauth2/token'
    refresh_token = None  

    token_manager = TokenManager(token_url, credentials, refresh_token)
    access_token = token_manager.get_token()
    return access_token

def create_export_report_csv(REPORT_ID):
    token = retrieve_access_token()
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/export/csv'
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()                                         # Raise an exception for bad status codes
    execution_id = response.json()['data']['executionId']
    return execution_id

def download_export_report_csv(REPORT_ID, execution_id):
    token = retrieve_access_token()
    headers = {'Authorization': f'Bearer {token}'}
    is_completed = False
    fibonacci_index = 1
    url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/exports/{execution_id}'

    while not is_completed:
        sleep_time = fibonacci(fibonacci_index)                         # Get the Fibonacci number
        fibonacci_index += 1                                            # Increment Fibonacci index for the next iteration
        print(f'Waiting {sleep_time} second(s)')
        time.sleep(sleep_time)                                          # Sleep for the Fibonacci number of seconds
        response = requests.get(url=url, headers=headers)               # Calls the endpoint to get report status
        response.raise_for_status()                                     # Raise an exception for bad status codes
        is_completed = (response.json()['data']['status']=='SUCCEEDED') # Check if finished

    url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/exports/{execution_id}/download'
    response = requests.get(url=url, headers=headers)                   # Calls the endpoint to download report zip file
    response.raise_for_status()                                         # Raise an exception for bad status codes
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref: # Unzips the content on the fly
        zip_ref.extractall('./')                                        # Saves into current folder
        return zip_ref.filelist

def main():
    '''Guess what, I'm the main module...'''

    # Adds custom parameters
    params = []
    if '--credentials'  in sys.argv: params.append('credentials')
    if '--reportid'     in sys.argv: params.append('reportid')

    # Retrieves all parameters
    args = getResolvedOptions(sys.argv, params)

    # Sets the report id and JOB_RUN_ID
    REPORT_ID = args['reportid'] if 'reportid' in args else '10e865fe-75d1-49a5-bec4-b0db905023e4'
    JOB_RUN_ID = int(time.time())

    # Runs the report and creates the csv
    execution_id = create_export_report_csv(REPORT_ID)

    # Downloads the zipped CSV
    filelist = download_export_report_csv(REPORT_ID, execution_id)
    
    s3client = boto3.client('s3')
    for csvfile in filelist:
        s3_filename = csvfile.filename
        with open(s3_filename, 'r') as file:
            csvcontent = file.read()
        upload_json_gz(glue_job_logger, s3client, S3_BUCKET, S3_PATH + f'{str(JOB_RUN_ID)}-{s3_filename}.gz', csvcontent)


if __name__ == "__main__":
    main()
