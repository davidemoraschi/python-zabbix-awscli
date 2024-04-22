import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3
import re
import json


# args = getResolvedOptions(sys.argv, ["JOB_NAME"])
args = getResolvedOptions(sys.argv, ['JOB_NAME', "destination_bucket", "origin_bucket"])
curated_bucket = args['destination_bucket']
source_bucket = args['origin_bucket']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
# set custom logging on
logger = glueContext.get_logger()
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
source_bucket_name = s3_resource.Bucket(source_bucket)

# # Source database and table
# SOURCE_DATABASE = "stg-dlk-prod-ds6-refined-db"

# # Destination S3 bucket, database and table
# CURATED_BUCKET_NAME = "stg-dlk-prod-cl-3-curated" 
# DESTINATION_DATABASE = "stg-dlk-prod-cl-3-curated-db"

# Get a list of source folders
def list_folders(s3_client, bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='', Delimiter='/')
    for content in response.get('CommonPrefixes', []):
        yield content.get('Prefix')

# Get the latest subfolder 
def get_latest_subfolder(s3_client, bucket_name, table_name):
    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=table_name
    )
    return response['Contents'][-1]['Key'].split('/')[-2]

source_tables = list_folders(s3_client, source_bucket)
logger.info("#"*20)
logger.info(f"Source tables: " + str(source_tables))


for source_table in source_tables:
    logger.info(f"Processing Table {source_table}")
    # Data source
    latest_folder = get_latest_subfolder(s3_client, source_bucket, source_table)
    
    S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
        format_options={},
        connection_type="s3",
        format="parquet",
        connection_options={
            "paths": [f"s3://{source_bucket}/{source_table}/{latest_folder}"],
            "recurse": True,
        },
        transformation_ctx="S3bucket_node1",
    )

############################################################################################################
    # Filter out a specific list of test users
    # First check which table has a email field
    spark_df = S3bucket_node1.toDF()

    # Regular expression pattern to match "email" substring
    pattern = r"^.*email$"

    valid_email_fields = [s for s in spark_df.columns if re.search(pattern, s, re.IGNORECASE)]

    if valid_email_fields:
        spark_df.createOrReplaceTempView("TEMP_DF")
        predicates = ""
        for field in valid_email_fields:
            predicates += f'''
                AND "{field}" NOT LIKE '%@straumann.com%'
                AND "{field}" NOT LIKE '%@im-systems.de%'
                AND "{field}" NOT LIKE '%@anthogyr.com%'
                AND "{field}" NOT LIKE '%@medentika.de%'
                AND "{field}" NOT LIKE '%@imsssde.de%'
                AND "{field}" NOT LIKE '%@ims.de%'
                AND "{field}" NOT LIKE '%@user.de%'
                AND "{field}" NOT LIKE '%@test.de%'
                AND "{field}" NOT LIKE '%@neodent.com%'
                AND "{field}" NOT LIKE '%@dental-wings.com%'
                AND "{field}" NOT LIKE '%@clearcorrect.com%'
                AND "{field}" NOT LIKE '%@private.ch%'
                AND "{field}" NOT LIKE '%@ch.ch%'
                AND "{field}" NOT LIKE '%@im-de.de%'
                AND "{field}" NOT LIKE '%@registrationtest.com%'
                AND "{field}" NOT LIKE '%@test562.it%'
                AND "{field}" NOT LIKE '%@rebelartistry.com%'
                AND "{field}" NOT LIKE '%@wearehackerone.com%'
                AND "{field}" NOT IN ('testuser@yahoo.com',
                                    'testing@six-group.com',
                                    'test@multi.de',
                                    'test.victim@example.com',
                                    'pegnevsales@aol.com',
                                    'tomasz.dzierzewicz@rebelartistry.com',
                                    'zejnilos@gmail.com',
                                    'aurinko_paistaa@registrationtest.com',
                                    'fmbarani@gmail.com',
                                    'TEST@gmail.com'
                                )
            '''
        spark_df = spark.sql("SELECT * FROM TEMP_DF WHERE True " + predicates)
############################################################################################################
    for obj in source_bucket_name.objects.filter(Prefix = "column_names/ds6_column_names"):
            body = obj.get()['Body'].read().decode('utf-8')
            json_content = json.loads(body)
            for column in json_content:
                if column in spark_df.columns:
                    new_column_name = json_content[column]
                    spark_df = spark_df.withColumnRenamed(column, new_column_name)
    glue_dynamic_frame = DynamicFrame.fromDF(spark_df, glueContext, "glue_dynamic_frame")
    # Data destination
    destination_table = source_table
    path=f"s3://{curated_bucket}/{destination_table}/"
    
    # Deletes files before writing new data
    glueContext.purge_s3_path(s3_path=path,  options={"retentionPeriod": 0})
    

    S3bucket_node2 = glueContext.write_dynamic_frame.from_options(
        frame=glue_dynamic_frame,
        connection_type="s3",
        format="glueparquet",
        connection_options={
            "path": path,
            "partitionKeys": [],
        },
        format_options={"compression": "snappy"},
        transformation_ctx="S3bucket_node3",
    )

    job.commit()