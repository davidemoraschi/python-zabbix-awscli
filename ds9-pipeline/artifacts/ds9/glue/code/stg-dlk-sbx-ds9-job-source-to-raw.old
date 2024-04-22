#!/usr/bin/python
'''
Testing the GSSDK
'''
import json
import boto3
from botocore.exceptions import ClientError
from typing import Dict
from gzip_s3_and_json_py3 import upload_json_gz
from config import S3_DESTINATION_BUCKET, S3_DESTINATION_PATH
import requests


def get_secret() -> Dict[str, str]:
    '''Retrieves the secret from AWS Secrets Manager'''

    secret_name: str = "stg/dlk/sapcdc/ds9/secrets"
    region_name: str = "eu-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    except ClientError as exc:
        raise exc

    secret: Dict[str, str] = get_secret_value_response['SecretString']
    return secret


def get_headers() -> Dict[str, str]:
    '''Returns the headers for the API requests'''

    return {"Content-Type": "application/x-www-form-urlencoded"}


creds: Dict[str, str] = json.loads(s=get_secret())  # type: ignore

APIKEY = creds['apiKey']
SECRETKEY = creds['secret']
USERKEY = creds['userKey']
BASEURL = creds['account.search']['URL']  # type: ignore
TIMEOUT = 60000
CONTEXT = 'awsglue'

headers: Dict[str, str] = get_headers()
sqlquery = 'SELECT%20UID%20AS%20i%20FROM%20accounts%20limit%2010000'
nextCursorId: str = None  # type: ignore
rooturl: str = f'{BASEURL}?apiKey={APIKEY}&userKey={USERKEY}&secret={SECRETKEY}&timeout={TIMEOUT}&context={CONTEXT}&httpStatusCodes=true'
objectscount = 0

# Creates boto3 session/client
glue_job_session = boto3.Session()
s3_client = glue_job_session.client(service_name='s3')

while True:
    # Construct API URL
    if nextCursorId:
        url = f'{rooturl}&cursorId={nextCursorId}'
    else:
        url = f'{rooturl}&query={sqlquery}&openCursor=true'

    # Make API request
    response: requests.Response = requests.post(url=url, headers=headers)

    # Raise an exception for bad status codes
    response.raise_for_status()

    result = json.loads(response.text)
    objectscount = objectscount+result['objectsCount']
    print(objectscount)

    # Uploads to S3 raw bucket/folder
    upload_json_gz(s3client=s3_client, bucket=S3_DESTINATION_BUCKET,
                   key=f'{S3_DESTINATION_PATH} account.search/{nextCursorId}.gz', obj=response.text)

    if 'nextCursorId' in result:
        nextCursorId = result['nextCursorId']
    else:
        break


# Make API request nextCursorId
response: requests.Response = requests.post(url=url, headers=headers)

# Raise an exception for bad status codes
response.raise_for_status()

result = json.loads(response.text)

print(result['objectsCount'])
