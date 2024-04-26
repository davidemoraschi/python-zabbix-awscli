#!/usr/bin/python
'''
# Python Shell jobs on AWS Glue:
# 1. Gets the latest JSON files from the bucket stg-dlk-sbx-ds-14-raw, folder events_feed/events_jsonl/
# 2. Downloads JSON file, extracts JSON array and recompress it (1DPU?)
# 3. Uploads to stg-dlk-sbx-ds-14-raw S3 bucket for further processing
# 4. Moves the original file to the folder events_feed/events_jsonl/processed
# davide.moraschi@toptal.com 2024
'''

# Import necessary modules
import json
import sys
import time
import boto3
from tabulate import tabulate
from common_functions import log, log_environment, process_arguments, send_sns, create_etl_log_table
from config import AWS_BUCKET, AWS_FOLDER, S3_DESTINATION_BUCKET, S3_DESTINATION_PATH, S3_PROCESSED_FOLDER
from gzip_s3_and_json_py3 import upload_json_gz
from typing import Dict, List
from typing import Any


events: Dict[str, str] = process_arguments(options=['EVENT_TYPES'])
EVENT_TYPES: List[str] = json.loads(events['EVENT_TYPES'])


def move_to_processed_folder(s3_client: Any, aws_bucket: str, from_file_key: Any, to_file_key: Any) -> None:
    '''Moves a file from one source folder to a destination one'''

    # Copy the file to the destination folder
    try:
        s3_client.copy_object(Bucket=aws_bucket, CopySource=aws_bucket + '/' + from_file_key.key, Key=S3_PROCESSED_FOLDER + to_file_key)
        # Delete the original file
        s3_client.delete_object(Bucket=aws_bucket, Key=from_file_key.key)
    except Exception as exc:
        # Log the exception
        log(str_message='ERROR', bigint_rows_retrieved=-1, str_error_message=f'str({exc})')
        raise


def main() -> None:
    '''Main function'''

    try:
        # Log environment information for debugging
        job_run_id, environment = log_environment()
        
        # Creates the log table if not exists
        create_etl_log_table(14)

        # Log start of job
        log(str_message='start-job')

        # Generate bucket name
        aws_bucket = AWS_BUCKET.replace('${var.env}',environment)

        # Creates boto3 session/client
        glue_job_session = boto3.Session()
        s3_client = glue_job_session.client(service_name='s3')

        # Creates a S3 resource and gets the bucket
        s3_resource = boto3.resource(service_name='s3')
        json_bucket = s3_resource.Bucket(name=aws_bucket)
        total_file_count = 0

        # Loops for every JSON file in the ext bucket/folder
        for json_file in json_bucket.objects.filter(Prefix=AWS_FOLDER):

            # Gets the file
            if not json_file.key.endswith('/'):  # Check if the file is not a folder
                # Gets the event type from the file name
                event_type = json_file.key.split(AWS_FOLDER)[1].split('/')[1].split('.')[1]
                if event_type in EVENT_TYPES:

                    # Log current file
                    log(str_message=f'Processing file:{json_file.key}')
                    total_file_count +=1
                    
                    # Reads the file
                    s3_file = s3_client.get_object(Bucket=aws_bucket, Key=json_file.key)
                    json_payload = s3_file['Body'].read().decode('utf-8')

                    # Log file upload
                    s3_filename: str = json_file.key.replace(AWS_FOLDER,'/') # json_file.key.split(AWS_FOLDER)[1].split('/') #[1]
                    log(str_message=f'Uploading file: {s3_filename}')

                    # Uploads to S3 raw bucket/folder
                    upload_json_gz(s3client=s3_client, bucket=S3_DESTINATION_BUCKET.replace('${var.env}',environment),
                                   key=S3_DESTINATION_PATH + event_type + '{0}.gz'.format(s3_filename), obj=json_payload)

                    # Moves it from the ext folder to the processed one
                    move_to_processed_folder(s3_client=s3_client,aws_bucket=aws_bucket, from_file_key=json_file, to_file_key=s3_filename)

        # Log succesful end of job
        log(str_message='end-job', bigint_rows_retrieved=total_file_count, str_error_message=f'Success.')

    except Exception as exc:
        # Log error
        log(str_message='ERROR', bigint_rows_retrieved=-1, str_error_message=f'str({exc})')

        # Send SNS notification of error
        send_sns(exc=exc)

        # Log failed end of job
        log(str_message='end-job', str_error_message=f'Failure.')

        # Reraise exception
        raise


# Run main function if script is run directly
if __name__ == "__main__":
    main()
