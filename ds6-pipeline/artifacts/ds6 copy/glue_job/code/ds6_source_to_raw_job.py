import json
import os
import math
from botocore.exceptions import ClientError
import logging
import urllib3
import boto3
import sys
from awsglue.utils import getResolvedOptions
from datetime import datetime

http = urllib3.PoolManager()
args = getResolvedOptions(sys.argv, ['report_id','startTime','docebo_api_url','bucket_name','credentials','region'])
    
report_id       = args['report_id']
startTime       = args['startTime']
docebo_api_url  = args['docebo_api_url']
credentials     = args['credentials']
bucket_name     = args['bucket_name']
region_name     = args['region']

# # Variables
pages = 0
fromp = 0
responselist = []

d = datetime.fromisoformat(startTime.replace('Z', '+00:00'))
ts = datetime.timestamp(d)

## Get Parameters
def get_parameter(parameter_name):

    session = boto3.session.Session()
    client = session.client(
        service_name='ssm'
    )

    try:
        get_parameter_response = client.get_parameter(
            Name=parameter_name,
            WithDecryption=True
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    parameter = get_parameter_response['Parameter']['Value']
    
    return parameter

## Get Secrets
def get_secret(secret_name):

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    
    return json.loads(secret)

retrieve_credentials = get_secret(credentials)

retrieve_docebo_api_url = get_parameter(docebo_api_url)
credentials_payload = json.dumps(retrieve_credentials)

# Token 
token_headers = {
  'Content-Type': 'application/json',
}
url_token = "https://{}/oauth2/token".format(retrieve_docebo_api_url)
response_token = http.request("POST", url_token, headers=token_headers, body=credentials_payload)
access_token = json.loads(response_token.data)["access_token"]

session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    region_name=region_name
)

#Report - Get response count
report_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(access_token),
}
url_report = "https://{}/report/v1/report/{}/count".format(retrieve_docebo_api_url,report_id)

payload = ""
response_report = http.request("GET", url_report, headers=report_headers, body=payload)

response_header = json.loads(response_report.data)

length = response_header.get('data').get("count")

pages = math.ceil(length/500)

for each in range(0, pages, 1):
    url_report_from = "https://learn.straumanngroup.com/report/v1/report/{}/data?from={}".format(report_id,fromp)
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(access_token),
    }

    response = http.request("GET", url_report_from, headers=headers, body=payload)

    response_dict = json.loads(response.data).get('data').get("rows")
    
    responselist.extend(response_dict)
    fromp = fromp+500

json_responselist = json.dumps(responselist)

s3_client.put_object(
    Body=json_responselist, # maybe json dump
    Bucket=bucket_name,
    Key=f"reportId={report_id}/date={int(ts)}/{report_id}.json"
)