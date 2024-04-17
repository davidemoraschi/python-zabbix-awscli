#!/usr/bin/env python3

import datetime
import json
import sys
import boto3
import pandas as pd
import webbrowser
from typing import Any
from tabulate import tabulate
from boto3.session import Session
from time import time, sleep


def serialize_datetime(obj: Any) -> str:
    '''Define a custom function to serialize datetime objects'''

    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def get_sso_session() -> Session:
    '''        
    # if your sso is setup in a different region, you will
    # want to include region_name=sso_region in the 
    # session constructor below
    '''
    session = Session(region_name='eu-central-1')
    account_id = '286719176505'
    start_url = 'https://d-996713059c.awsapps.com/start/#'
    region = 'eu-west-1'
    sso_oidc = session.client('sso-oidc')
    client_creds = sso_oidc.register_client(clientName='myapp', clientType='public',)
    device_authorization = sso_oidc.start_device_authorization(
        clientId=client_creds['clientId'],
        clientSecret=client_creds['clientSecret'],
        startUrl=start_url,
    )
    url = device_authorization['verificationUriComplete']
    device_code = device_authorization['deviceCode']
    expires_in = device_authorization['expiresIn']
    interval = device_authorization['interval']
    webbrowser.open(url, autoraise=True)
    for n in range(1, expires_in // interval + 1):
        sleep(interval)
        try:
            token = sso_oidc.create_token(
                grantType='urn:ietf:params:oauth:grant-type:device_code',
                deviceCode=device_code,
                clientId=client_creds['clientId'],
                clientSecret=client_creds['clientSecret'],
            )
            break
        except sso_oidc.exceptions.AuthorizationPendingException:
            pass

    access_token = token['accessToken']
    sso = session.client('sso')
    account_roles = sso.list_account_roles(
        accessToken=access_token,
        accountId=account_id,
    )
    roles = account_roles['roleList']
    # simplifying here for illustrative purposes
    role = roles[0]

    # earlier versions of the sso api returned the
    # role credentials directly, but now they appear
    # to be in a subkey called `roleCredentials`
    role_creds = sso.get_role_credentials(
        roleName=role['roleName'],
        accountId=account_id,
        accessToken=access_token,
    )['roleCredentials']
    session = Session(
        region_name=region,
        aws_access_key_id=role_creds['accessKeyId'],
        aws_secret_access_key=role_creds['secretAccessKey'],
        aws_session_token=role_creds['sessionToken'],
    )
    return session


def main() -> None:
    '''Main function'''

    profile_session: boto3.Session = get_sso_session()  # boto3.Session(region_name='eu-west-1', profile_name='dBeaver_prod')
    jobname: str = 'stg-dlk-prod-ds7-job-raw-to-refined'
    glueclient = profile_session.client(service_name='glue')
    response = glueclient.get_job_runs(JobName=jobname, MaxResults=30)
    # payload: str = json.dumps(response['JobRuns'], default=serialize_datetime)
    # print(payload)

    df = pd.DataFrame(response['JobRuns'])
    print(df)
    # print(df[['JobName', 'JobRunState', 'StartedOn', 'CompletedOn', 'ExecutionTime', 'MaxCapacity', 'WorkerType', 'ErrorMessage', 'Arguments']])
    # print(tabulate(
    #     tabular_data=df[['JobName', 'JobRunState', 'StartedOn', 'CompletedOn', 'ExecutionTime', 'MaxCapacity', 'WorkerType', 'ErrorMessage', 'Arguments']],
    #     headers="keys", showindex=False))


if __name__ == "__main__":
    main()
