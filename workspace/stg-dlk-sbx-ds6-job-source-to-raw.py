#!/usr/bin/python
'''
Python Shell jobs on AWS Glue:
1. Does a POST API call to create a token
2. Uses the token to authenticate to another API and start creating an export file
3. Checks for execution and when done downloads the CSV result
davide.moraschi@toptal.com 2024
'''

import sys

import requests
from awsglue.utils import getResolvedOptions
from gzip_s3_and_json_py3 import get_secret_credentials
from config import AWS_REGION, AWS_SECRET_NAME
from TokenManager import TokenManager

params = []

def retrieve_access_token():
    credentials = get_secret_credentials(AWS_REGION, AWS_SECRET_NAME)
    token_url = 'https://clearcorrect.docebosaas.com/oauth2/token'
    refresh_token = None  

    token_manager = TokenManager(token_url, credentials, refresh_token)
    access_token = token_manager.get_token()
    return access_token

    #print(access_token)

    # ri_access_token = token_manager.get_token()
    # print(ri_access_token)
    
    # tri_access_token = token_manager.get_token(credentials)
    # print(tri_access_token)

    #print(token_manager.is_token_valid())

def main():
    '''Guess what, I'm the main module...'''

    if '--credentials' in sys.argv:
        params.append('credentials')
    # if '--JOB_NAME' in sys.argv:
    #     params.append('JOB_NAME')
    args = getResolvedOptions(sys.argv, params)

    # if 'JOB_NAME' in args:
    #     JOB_NAME = args['JOB_NAME']
    # else:
    #     JOB_NAME = 'stg-dlk-sbx-ds11-job-source-to-raw'

    # JOB_RUN_ID = int(time.time())
    REPORT_ID = '10e865fe-75d1-49a5-bec4-b0db905023e4'

    token = retrieve_access_token()
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://clearcorrect.docebosaas.com/analytics/v1/reports/{REPORT_ID}/export/csv'
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        execution_id = response.json()['data']['executionId']
        print(execution_id)

if __name__ == "__main__":
    main()
