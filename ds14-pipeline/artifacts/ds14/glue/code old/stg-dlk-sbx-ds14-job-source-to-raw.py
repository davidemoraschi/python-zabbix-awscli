#!/usr/bin/python
'''
# Python Shell jobs on AWS Glue:
# 1. Gets the latest JSON files from the bucket stg-dlk-sbx-ds-14-raw, folder events_feed/events_jsonl/
# 2. Downloads JSON file, extracts JSON array and recompress it (1DPU?)
# 3. Uploads to stg-dlk-sbx-ds-14-raw S3 bucket for further processing (deletes original file?)
# davide.moraschi@toptal.com 2024
'''

# Import necessary modules
import json
import sys
import time
import boto3
from tabulate import tabulate
from common_functions import log, log_environment, process_arguments, send_sns
from config import AWS_BUCKET, AWS_FOLDER, S3_DESTINATION_BUCKET, S3_DESTINATION_PATH, S3_PROCESSED_FOLDER
from gzip_s3_and_json_py3 import upload_json_gz
from typing import Dict, List
from typing import Any

# Process command line arguments
args: Dict[str, str] = process_arguments(options=['WORKFLOW_NAME', 'WORKFLOW_RUN_ID', 'EVENT_TYPES'])

# Print arguments for debugging
print(tabulate(tabular_data=args.items(), headers=['args.keys()', 'args.values()'], tablefmt='psql', showindex=False))

# Parse report IDs, workflow name, EVENT_TYPES, and job name from arguments
EVENT_TYPES: List[str] = json.loads(args['EVENT_TYPES'])
WORKFLOW_NAME: str = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID: str = args['WORKFLOW_RUN_ID']
JOB_NAME: str = args['JOB_NAME'] if 'JOB_NAME' in args else 'stg-dlk-sbx-ds14-job-source-to-raw'
JOB_RUN_ID: int = int(time.time())


def move_to_processed_folder(s3_client: Any, from_file_key: Any, to_file_key: Any) -> None:
    '''Moves a file from one source folder to a destination one'''

    # Copy the file to the destination folder
    try:
        s3_client.copy_object(Bucket=AWS_BUCKET, CopySource=AWS_BUCKET + '/' + from_file_key.key, Key=S3_PROCESSED_FOLDER + to_file_key)
        # Delete the original file (commented out)
        # s3_client.delete_object(Bucket=AWS_BUCKET, Key=from_file_key.key)
    except Exception as exc:
        # Log the exception
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message=f'An error occurred:{str(exc)}')
        raise


def main() -> None:
    '''Main function'''

    try:
        # Log environment information for debugging
        log_environment()

        # Log start of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message='start-job')

        # Creates boto3 session/client
        glue_job_session = boto3.Session()
        s3_client = glue_job_session.client(service_name='s3')

        # Creates a S3 resource and gets the bucket
        s3_resource = boto3.resource(service_name='s3')
        json_bucket = s3_resource.Bucket(name=AWS_BUCKET)

        # Loops for every JSON file in the ext bucket/folder
        for json_file in json_bucket.objects.filter(Prefix=AWS_FOLDER):

            # Gets the file
            if not json_file.key.endswith('/'):  # Check if the file is not a folder
                # Gets the event type from the file name
                event_type = json_file.key.split(AWS_FOLDER)[1].split('/')[1].split('.')[1]
                if event_type in EVENT_TYPES:
                    # Reads the file
                    s3_file = s3_client.get_object(Bucket=AWS_BUCKET, Key=json_file.key)
                    json_payload = s3_file['Body'].read().decode('utf-8')

                    # Log file upload
                    s3_filename: str = json_file.key.split(AWS_FOLDER)[1].split('/')[1]
                    log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
                        job_run_id=str(JOB_RUN_ID), str_message=f'Uploading file: {s3_filename}')

                    # Uploads to S3 raw bucket/folder
                    upload_json_gz(s3client=s3_client, bucket=S3_DESTINATION_BUCKET,
                                   key=S3_DESTINATION_PATH + event_type + '/{0}.gz'.format(s3_filename), obj=json_payload)

                    # Moves it from the ext folder to the processed one
                    move_to_processed_folder(s3_client=s3_client, from_file_key=json_file, to_file_key=s3_filename)

        # Log end of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message='end-job')

    except Exception as exc:
        # Log error
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message=f'An error occurred:{str(exc)}')

        # Send SNS notification of error
        send_sns(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
                 job_run_id=str(JOB_RUN_ID), exc=exc)

        # Log end of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message='end-job')

        # Reraise exception
        # sys.exit(1)
        raise


# Run main function if script is run directly
if __name__ == "__main__":
    main()
    # sys.exit(0)
