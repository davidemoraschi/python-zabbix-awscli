#!/usr/bin/python
'''
# Python Shell jobs on AWS Glue:
# 1. Does a POST API call to create a token
# 2. Uses the token to authenticate to another API and start creating an export file
# 3. Checks for execution and when done downloads the CSV result
# davide.moraschi@toptal.com 2024
'''

# Import necessary libraries
import io
import json
import time
import zipfile
import boto3
import requests
from tabulate import tabulate
from common_functions import log, log_environment, process_arguments, fibonacci, send_sns
from gzip_s3_and_json_py3 import upload_json_gz, get_headers
from config import S3_BUCKET, S3_PATH
from typing import Dict, List

# Process command line arguments
args: Dict[str, str] = process_arguments(options=['WORKFLOW_NAME', 'WORKFLOW_RUN_ID', 'REPORT_IDS'])

# Print arguments for debugging
print(tabulate(tabular_data=args.items(), headers=['args.keys()', 'args.values()'], tablefmt='psql', showindex=False))

# Parse report IDs, workflow name, run ID, and job name from arguments
REPORT_IDS: List[str] = json.loads(args['REPORT_IDS'])
WORKFLOW_NAME: str = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID: str = args['WORKFLOW_RUN_ID']
JOB_NAME: str = args['JOB_NAME'] if 'JOB_NAME' in args else 'stg-dlk-sbx-ds6-job-source-to-raw'
JOB_RUN_ID: int = int(time.time())

def create_export_report_csv(report_id: str) -> str:
    '''Calls the Docebo API to start a report extraction'''

    try:
        # Get headers for API request
        headers: Dict[str, str] = get_headers()

        # Construct API URL
        url: str = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{report_id}/export/csv'

        # Make API request
        response: requests.Response = requests.get(url=url, headers=headers)

        # Raise an exception for bad status codes
        response.raise_for_status()

        # Extract execution ID from response
        execution_id: str = response.json()['data']['executionId']

        return execution_id
    except requests.exceptions.HTTPError as exc:
        raise

def download_export_report_csv(REPORT_ID: str, execution_id: str) -> List[zipfile.ZipInfo]:
    '''Calls the Docebo API to download the report zip file'''

    try:
        # Get headers for API request
        headers: Dict[str, str] = get_headers()

        # Initialize completion flag and Fibonacci index
        is_completed: bool = False
        fibonacci_index: int = 1

        # Construct API URL
        url: str = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/exports/{execution_id}'

        while not is_completed:
            # Calculate sleep time using Fibonacci sequence
            sleep_time: int = fibonacci(fibonacci_index)

            # Increment Fibonacci index for the next iteration
            fibonacci_index += 1

            # Sleep for the Fibonacci number of seconds
            time.sleep(sleep_time)

            # Make API request to get report status
            response: requests.Response = requests.get(url=url, headers=headers)

            # Raise an exception for bad status codes
            response.raise_for_status()

            # Check if report generation has finished
            is_completed = (response.json()['data']['status'] == 'SUCCEEDED')

        # Construct download URL
        url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/exports/{execution_id}/download'

        # Make API request to download report zip file
        response = requests.get(url=url, headers=headers)

        # Raise an exception for bad status codes
        response.raise_for_status()

        # Unzip the content on the fly and save into current folder
        with zipfile.ZipFile(file=io.BytesIO(initial_bytes=response.content), mode='r') as zip_ref:
            zip_ref.extractall('./')

            return zip_ref.filelist
    except requests.exceptions.HTTPError as exc:
        raise

def main() -> None:
    '''Main function'''

    try:
        # Log environment information for debugging
        log_environment()

        # Log start of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=JOB_RUN_ID, str_message='start-job')

        # Process each report ID
        for report_id in REPORT_IDS:
            # Log current report ID
            log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
                job_run_id=JOB_RUN_ID, str_message=f'Running report_id:{report_id}')

            # Run report and create CSV
            execution_id: str = create_export_report_csv(report_id=report_id)

            # Download zipped CSV
            filelist: List[zipfile.ZipInfo] = download_export_report_csv(
                report_id, execution_id)

            # Create S3 client for uploading to raw bucket
            s3client = boto3.client('s3')

            # Process each CSV file
            for csvfile in filelist:
                # Construct S3 filename
                s3_filename: str = csvfile.filename

                # Open CSV file and read content
                with open(file=s3_filename, mode='r') as file:
                    csvcontent: str = file.read()

                # Log file upload
                log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
                    job_run_id=JOB_RUN_ID, str_message=f'Uploading file: {s3_filename}')

                # Upload file to S3
                upload_json_gz(s3client=s3client, bucket=S3_BUCKET,
                               key=S3_PATH + f'{str(JOB_RUN_ID)}-{s3_filename}.gz', obj=csvcontent)

        # Log end of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=JOB_RUN_ID, str_message='end-job')

    except Exception as exc:
        # Log error
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=JOB_RUN_ID, str_message=f'An error occurred:{str(exc)}')

        # Send SNS notification of error
        send_sns(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
                 job_run_id=JOB_RUN_ID, exc=exc)

        # Log end of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=JOB_RUN_ID, str_message='end-job')

        # Reraise exception
        raise

# Run main function if script is run directly
if __name__ == "__main__":
    main()
