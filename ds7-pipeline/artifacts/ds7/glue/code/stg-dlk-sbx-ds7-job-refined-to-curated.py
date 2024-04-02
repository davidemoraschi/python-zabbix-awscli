from pyspark.sql.types import *
from pyspark.conf import SparkConf
from pyspark.sql.functions import last, sum, substring
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark import SparkContext
from awsglue.utils import getResolvedOptions
import sys

args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "table_name",
        "source_db_name",
        "destination_db_name",
        "destination_bucket",
        "partcol",
        "origin_bucket",
    ],
)
job_name = args["JOB_NAME"]

table_name = args["table_name"]
partition_columns = [args["partcol"].lower()]

source_db_name = args["source_db_name"]
destination_db_name = args["destination_db_name"]

raw_bucket_name = args["origin_bucket"]
refined_bucket_name = args["destination_bucket"]


sc = SparkContext()
glueContext = GlueContext(sc)
logger = glueContext.get_logger()
spark = glueContext.spark_session
job = Job(glueContext)
# job.init(job_name, args)

# Prepare for the custom table name #awswebregform
if "contact" in table_name:
    custom_table_name = "ds7_sap_mktcloud_contact"
elif "explicitpermission" in table_name:
    custom_table_name = "ds7_sap_mktcloud_explicitpermission"
elif "initiative" in table_name or "intiative" in table_name:
    custom_table_name = "ds7_sap_mktcloud_initiative"
elif "assgdcmpgnsuccessdata" in table_name:
    custom_table_name = "ds7_sap_mktcloud_assgdcmpgnsuccessdata"
elif "interaction" in table_name:
    custom_table_name = "ds7_sap_mktcloud_interaction"
    partition_columns = ["interactiontimestamputc"]
elif "awswebregform" in table_name:
    custom_table_name = "ds7_sap_mktcloud_awswebregform"
    partition_columns = ["interactiontimestamputc"]

ddf = glueContext.create_dynamic_frame.from_catalog(
    database=source_db_name,
    table_name=table_name,
)

# Convert column names to lower case
df = ddf.toDF()
df = df.select([col.lower() for col in df.columns])
lower_column_names = df.columns

# Check if partition columns are available in the schema
# if not, write data without partition
for column in partition_columns.copy():
    if column not in lower_column_names:
        partition_columns.remove(column)
        logger.error(f"### Partition column {column} does not exist. Removed.")

partition_columns.clear()  # TODD: No partion for now, might need to remove it in the future.

ddf = DynamicFrame.fromDF(df, glueContext, "ddf")

sink = glueContext.getSink(
    path=f"s3://{refined_bucket_name}/{custom_table_name}/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=partition_columns,
    compression="snappy",
    enableUpdateCatalog=True,
)

sink.setCatalogInfo(
    catalogDatabase=destination_db_name,
    catalogTableName=custom_table_name,
)

sink.setFormat("glueparquet")
sink.writeFrame(ddf)

job.commit()
