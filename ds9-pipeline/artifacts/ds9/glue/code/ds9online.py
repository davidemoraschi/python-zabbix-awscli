#!/usr/bin/python
'''
Testing the SAP CDC API to get the audit logs
'''

import json
import os
import time
import boto3
from tabulate import tabulate
from botocore.exceptions import ClientError
from typing import Dict
from gzip_s3_and_json_py3 import upload_json_gz
from common_functions import get_last_loaded_epoch, log, process_arguments
from config import S3_DESTINATION_BUCKET, S3_DESTINATION_PATH, AWS_SECRET_NAME, AWS_REGION
import requests
import jq
from typing import Dict, List

# Process command line arguments
args: Dict[str, str] = process_arguments(options=['WORKFLOW_NAME', 'WORKFLOW_RUN_ID'])

# Print arguments for debugging
print(tabulate(tabular_data=args.items(), headers=['args.keys()', 'args.values()'], tablefmt='psql', showindex=False))

# Parse report IDs, workflow name, EVENT_TYPES, and job name from arguments
WORKFLOW_NAME: str = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID: str = args['WORKFLOW_RUN_ID']
JOB_NAME: str = args['JOB_NAME'] if 'JOB_NAME' in args else 'stg-dlk-sbx-ds9-job-source-to-raw'
JOB_RUN_ID: int = int(time.time())


TIMEOUT = 60000
ROWLIMIT = 10000
JOB_RUN_ID: int = int(time.time())


def get_secret() -> Dict[str, str]:
    '''
    Retrieves the secret from AWS Secrets Manager

    Returns:
        A dictionary containing the secret values.
    '''
    secret_name: str = AWS_SECRET_NAME
    region_name: str = AWS_REGION

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    except ClientError as exc:
        raise exc

    secret: Dict[str, str] = get_secret_value_response['SecretString']
    return secret


creds: Dict[str, str] = json.loads(s=get_secret())  # type: ignore
BASEURL = creds['audit.search']['URL']              # type: ignore


def get_headers() -> Dict[str, str]:
    '''
    Returns the headers for the API requests

    Returns:
        A dictionary containing the headers.
    '''
    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "deflate, gzip;q=1.0, *;q=0.5"
    }


def get_params() -> Dict[str, str]:
    '''
    Returns the parameters for the API requests

    Returns:
        A dictionary containing the parameters.
    '''
    params: dict = {}
    params["secret"] = creds['secret']
    params["userKey"] = creds['userKey']
    params["apiKey"] = creds['apiKey']
    params["httpStatusCodes"] = True
    params["checkParams"] = True

    return params


def get_latest_epoch() -> float:
    '''
    Returns the latest epoch timestamp from the audit table
    '''
    headers: Dict[str, str] = get_headers()
    params: Dict[str, str] = get_params()
    # I know the ORDER BY here is an aberration, but without it the API returns NULL, so complain to SAP
    params['query'] = "SELECT max(@timestamp) AS latest_epoch FROM auditLog ORDER BY @timestamp DESC"

    response: requests.Response = requests.post(url=BASEURL, headers=headers, params=params)
    response.raise_for_status()
    payload: Dict[str, str] = json.loads(response.text)
    return payload['results'][0]['latest_epoch']   


def main():
    '''
    Main function that executes the script.
    '''
    nextCursorId: str = None                                # type: ignore
    headers: Dict[str, str] = get_headers()
    params: Dict[str, str] = get_params()
    objectscount: int = 0
    if os.path.exists('payload.json'):
        os.remove('payload.json')

    latest_epoch:float = get_latest_epoch()
    last_loaded_epoch:float = get_last_loaded_epoch()

    while True:

        # Adds pagination parameters
        if nextCursorId:
            params['cursorId'] = nextCursorId
            if params.get('query'):
                params.pop('query')
                params.pop('openCursor')

        else:
            params['openCursor'] = True                    # type: ignore
            params['query'] = f"SELECT * FROM auditLog \
                                WHERE (@timestamp > {last_loaded_epoch} and @timestamp <= {latest_epoch})\
                                LIMIT {ROWLIMIT}"

        # Make API request
        response: requests.Response = requests.post(url=BASEURL, headers=headers, params=params)

        # Raise an exception for bad status codes
        response.raise_for_status()
        payload = json.loads(response.text)

        objectscount += payload['objectsCount']
        totalCount = payload['totalCount']
        print(f'{objectscount} of {totalCount} rows')

        with open('payload.json', 'a') as file:
            jsonl = jq.compile(".[]").input_value(payload['results']).text()
            file.write(jsonl)
            
            # check if the end of the result
            if ('nextCursorId' not in payload) or (objectscount==payload['totalCount']):
                # isSucceeded = True
                # saveJSON.write(f"{json.dumps(tempOutput)[1:]}")
                break
            else:
                file.write('\n')
                # remove the {} and add a comma
                # saveJSON.write(f"{json.dumps(tempOutput)[1:-1]},")
                nextCursorId = payload['nextCursorId']
    
    with open('payload.json', 'r') as file:
        jsonl = file.read()

    # Creates boto3 session/client
    glue_job_session = boto3.Session()
    s3_client = glue_job_session.client(service_name='s3')

    # Uploads to S3 raw bucket/folder
    upload_json_gz(s3client=s3_client, bucket=S3_DESTINATION_BUCKET,
                   key=f'{S3_DESTINATION_PATH}{JOB_RUN_ID}.json.gz', obj=jsonl)

    log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
        job_run_id=str(JOB_RUN_ID), str_message=f'Uploading file: {JOB_RUN_ID}.json.gz', bigint_rows_retrieved=objectscount, float_latest_epoch=latest_epoch)


if __name__ == "__main__":
    main()
