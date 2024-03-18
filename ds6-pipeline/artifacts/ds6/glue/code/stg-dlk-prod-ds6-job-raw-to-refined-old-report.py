import boto3
import json
import re
import sys
import requests

import boto3
import json
import re
import sys
import requests

from pyspark.sql import SparkSession
from botocore.exceptions import ClientError
from botocore.exceptions import ClientError
from awsglue.utils import getResolvedOptions




spark = SparkSession.builder \
    .appName('DLK') \
    .config("fs.s3.canned.acl", "BucketOwnerFullControl") \
    .config("spark.sql.session.timeZone", "UTC") \
    .enableHiveSupport() \
    .getOrCreate()

args = getResolvedOptions(sys.argv, ['ENV', 'docebo_api_url', 'credentials', 'region'])
args = getResolvedOptions(sys.argv, ['ENV', 'docebo_api_url', 'credentials', 'region'])
ENV = args['ENV']
credentials = args['credentials']
docebo_api_url  = args['docebo_api_url']
region_name     = args['region']
credentials = args['credentials']
docebo_api_url  = args['docebo_api_url']
region_name     = args['region']
RAW_BUCKET_NAME = f"stg-dlk-{ENV}-ds-6-raw"
REFINED_BUCKET_NAME = f"stg-dlk-{ENV}-ds-6-refined"

def list_folders_in_s3(bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='', Delimiter='/')
    for content in response.get('CommonPrefixes', []):
        yield content.get('Prefix')

# Retrieve the customized column names by calling two additional APIs
## Get Parameters
def get_parameter(parameter_name):
    session = boto3.session.Session()
    client = session.client(service_name='ssm')
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

def get_additional_column_names(url, access_token):
    payload = ""
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(access_token),
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


retrieve_credentials = get_secret(credentials)

retrieve_docebo_api_url = get_parameter(docebo_api_url)
credentials_payload = json.dumps(retrieve_credentials)

# Token 
token_headers = {
  'Content-Type': 'application/json',
}
url_token = "https://{}/oauth2/token".format(retrieve_docebo_api_url)
# response_token = http.request("POST", url_token, headers=token_headers, body=credentials_payload)
response = requests.request("POST", url_token, headers=token_headers, data=credentials_payload)
# access_token = json.loads(response_token.data)["access_token"]
access_token = response.json()["access_token"]

## Mappings for customized columns
# Create id to column name mapping for course-level column names
docebo_course_api = "https://learn.straumanngroup.com/learn/v1/courses/field"
response = get_additional_column_names(docebo_course_api, access_token)
course_level_columns = {}
for x in response["data"]["items"]:
    course_level_columns[x['id']] = "course_" + x['name']['value'].lower().replace(" ", "_").replace(",", "")

# Create id to column name mapping for user-level column names
docebo_user_api = "https://clearcorrect.docebosaas.com/manage/v1/user/importer_fields"
response = get_additional_column_names(docebo_user_api, access_token)
user_level_columns = {}
user_level_columns = response["data"]["fields"]
user_level_columns['field_65'] = "city_2"
user_level_columns['field_63'] = "zip_code_2"


regex_course = re.compile(r'course_field_(\d+)_value')
regex_user = re.compile(r'^(field_\d+)_value')

def replace_course_col(match):
    return course_level_columns[int(match.group(1))].replace("(", "").replace(")", "")

def replace_user_col(match):
    return "user_" + user_level_columns[match.group(1)].lower().replace(" ", "_")\
      .replace(",", "").replace("(", "").replace(")", "")

folder_list = list_folders_in_s3(RAW_BUCKET_NAME)
partition_column = "date"
for folder in folder_list:
    report_id = folder.split('=')[1][:-1]
    INPUT_LOC = f"s3a://{RAW_BUCKET_NAME}/reportId={report_id}/"
    OUTPUT_LOC = f"s3a://{REFINED_BUCKET_NAME}/reportId={report_id}/"

    df = spark.read \
        .option("multiline", "true") \
        .json(INPUT_LOC)
    
    for col in df.columns:
        if regex_course.match(col): # if the column name match the pattern
            df = df.withColumnRenamed(col, re.sub(regex_course, replace_course_col, col))
            
        elif regex_user.match(col):
            df = df.withColumnRenamed(col, re.sub(regex_user, replace_user_col, col))
        else:
            pass
    
    for col in df.columns:
        if regex_course.match(col): # if the column name match the pattern
            df = df.withColumnRenamed(col, re.sub(regex_course, replace_course_col, col))
            
        elif regex_user.match(col):
            df = df.withColumnRenamed(col, re.sub(regex_user, replace_user_col, col))
        else:
            pass

    df.write.partitionBy(partition_column.lower()).mode("overwrite").parquet(OUTPUT_LOC)