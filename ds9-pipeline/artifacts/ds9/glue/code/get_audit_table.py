#!/usr/bin/python
'''
Testing the GSSDK
'''

import json
import boto3
from botocore.exceptions import ClientError
from typing import Dict
# from gzip_s3_and_json_py3 import upload_json_gz
# from config import S3_DESTINATION_BUCKET, S3_DESTINATION_PATH
import requests
import jq


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


creds: Dict[str, str] = json.loads(s=get_secret())  # type: ignore
BASEURL = creds['audit.search']['URL']              # type: ignore
TIMEOUT = 60000
CONTEXT = 'awsglue'
ROWLIMIT = 10


def get_headers() -> Dict[str, str]:
    '''Returns the headers for the API requests'''

    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "deflate, gzip;q=1.0, *;q=0.5"
    }


def get_params() -> Dict[str, str]:
    '''Returns the parameters for the API requests'''

    params: dict = {}
    params["secret"] = creds['secret']
    params["userKey"] = creds['userKey']
    params["apiKey"] = creds['apiKey']
    params["httpStatusCodes"] = True

    return params


def main():
    '''Main function that executes the script.'''

    nextCursorId: str = None                                # type: ignore
    headers: Dict[str, str] = get_headers()
    params: Dict[str, str] = get_params()
    objectscount: int = 0

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
                                WHERE (@timestamp >= '2024-03-20T00:00:00.000Z' and @timestamp < '2024-03-21T00:00:00.000Z')\
                                LIMIT {ROWLIMIT}"

        # Make API request
        response: requests.Response = requests.post(url=BASEURL, headers=headers, params=params)

        # Raise an exception for bad status codes
        response.raise_for_status()
        payload = json.loads(response.text)

        objectscount += payload['objectsCount']
        print(objectscount)

        with open('payload.json', 'a') as file:
            jsonl = jq.compile(".[]").input_value(payload['results']).text()
            file.write(jsonl)

        # check if the end of the result
        if payload['nextCursorId'] is None:
            # isSucceeded = True
            # saveJSON.write(f"{json.dumps(tempOutput)[1:]}")
            break
        else:
            # remove the {} and add a comma
            # saveJSON.write(f"{json.dumps(tempOutput)[1:-1]},")
            nextCursorId = payload['nextCursorId']


if __name__ == "__main__":
    main()
