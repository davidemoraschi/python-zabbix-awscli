data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# Define the provider and AWS region
provider "aws" {
  region  = "eu-west-1"
  profile = "816247855850_AdministratorAccess"
}

variable "datasource_number" {
  type    = string
  default = "11"
}

locals {
  datasource               = "ds${var.datasource_number}"
  ext_bucket_name          = "stg-dlk-sbx-ds-${var.datasource_number}-ext"
  raw_bucket_name          = "stg-dlk-sbx-ds-${var.datasource_number}-raw"
  datasource_bucket_folder = "events_feed/events_jsonl_gzip/"
  artifacts_bucket_name    = "stg-dlk-sbx-code-artifacts"
  database_name            = "stg-dlk-sbx-ds${var.datasource_number}-raw-db"
  role_name                = "stg-dlk-sbx-ds${var.datasource_number}-source-to-raw-glue-job-role"
  script_name              = "stg-dlk-sbx-ds${var.datasource_number}-job-source-to-raw"
  kms_key_arn              = "arn:aws:kms:eu-west-1:816247855850:key/396cd8ff-4b3d-4b17-9df4-9449185fdd2e"
}

resource "aws_s3_bucket" "bucket" {
  bucket              = local.raw_bucket_name
  force_destroy       = true
  object_lock_enabled = false
}

resource "aws_s3_bucket_public_access_block" "bucket_access_block" {
  bucket                  = aws_s3_bucket.bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_iam_role" "role" {
  name               = local.role_name
  # assume_role_policy = templatefile("./trust-policy.json", { service = "glue.amazonaws.com" })
  assume_role_policy = templatefile("${path.module}/artifacts/ds11/glue/policies/trust-policy.json", { service = "glue.amazonaws.com" })
}

resource "aws_iam_policy" "role_policy" {
  name = "${local.role_name}_policy"
  # policy = templatefile("./glue-role-policy.json", {
  policy = templatefile("${path.module}/artifacts/ds11/glue/policies/glue-role-policy.json", {  
    account_id       = data.aws_caller_identity.current.account_id
    region           = data.aws_region.current.name
    resource-arn     = aws_s3_bucket.bucket.arn
    ext-resource-arn = "arn:aws:s3:::${local.ext_bucket_name}"
    db_name          = local.database_name
  kms_key_arn = local.kms_key_arn })
}

resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  role       = aws_iam_role.role.name
  policy_arn = aws_iam_policy.role_policy.arn
}

resource "aws_lakeformation_resource" "data_location" {
  arn      = aws_s3_bucket.bucket.arn
  role_arn = aws_iam_role.role.arn
}

resource "aws_glue_catalog_database" "glue_database" {
  name         = local.database_name
  description  = "Glue catalog db for ${local.datasource} raw zone."
  location_uri = "s3://${local.raw_bucket_name}"
}

resource "aws_lakeformation_permissions" "database_permissions" {
  principal   = aws_iam_role.role.arn
  permissions = ["CREATE_TABLE", "DESCRIBE"]
  database {
    name = aws_glue_catalog_database.glue_database.name
  }
}

resource "aws_lakeformation_permissions" "tables_permissions" {
  principal   = aws_iam_role.role.arn
  permissions = ["ALL"]
  table {
    database_name = aws_glue_catalog_database.glue_database.name
    wildcard      = true
  }
}

resource "aws_glue_catalog_table" "events_jsonl_gzip" {
  name          = "events_jsonl_gzip"
  database_name = aws_glue_catalog_database.glue_database.name
  table_type    = "EXTERNAL_TABLE"
  parameters    = { "EXTERNAL" = "TRUE" }
  storage_descriptor {
    location      = "s3://${local.raw_bucket_name}/${local.datasource_bucket_folder}"
    input_format  = "org.apache.hadoop.mapred.TextInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat"
    ser_de_info {
      name                  = "json_serde"
      serialization_library = "org.openx.data.jsonserde.JsonSerDe"
      parameters            = { "paths" = "cdpid,firstname,lastname,profession,lettersalutation" }
    }
    columns {
      name = "crmid"
      type = "string"
    }
    columns {
      name = "firstname"
      type = "string"
    }
    columns {
      name = "lastname"
      type = "string"
    }
    columns {
      name = "profession"
      type = "string"
    }
    columns {
      name = "lettersalutation"
      type = "string"
    }
  }
}

resource "aws_s3_object" "glue_job_script" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/${local.script_name}.py"
  source      = "${path.module}/artifacts/ds11/glue/code/${local.script_name}.py"
  source_hash = filemd5("${path.module}/artifacts/ds11/glue/code/${local.script_name}.py")
}

resource "aws_s3_object" "glue_job_config" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/config.py"
  source      = "${path.module}/artifacts/ds11/glue/code/config.py"
  source_hash = filemd5("${path.module}/artifacts/ds11/glue/code/config.py")
}

resource "aws_s3_object" "glue_job_common_functions" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/common_functions.py"
  source      = "${path.module}/artifacts/ds11/glue/code/common_functions.py"
  source_hash = filemd5("${path.module}/artifacts/ds11/glue/code/common_functions.py")
  # etag               = filemd5("../common_functions.py")
}

resource "aws_s3_object" "glue_job_gzip_s3_and_json" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/gzip_s3_and_json_py3.py"
  source      = "${path.module}/artifacts/ds11/glue/code/gzip_s3_and_json_py3.py"
  source_hash = filemd5("${path.module}/artifacts/ds11/glue/code/gzip_s3_and_json_py3.py")
  # etag               = filemd5("../gzip_s3_and_json_py3.py")
}

resource "aws_glue_job" "glue_job" {
  name                            = local.script_name
  description                     = "Part 1 of SAP CDP. Strips the outer array from the JSON and uploads it to the stg-dlk-sbx-ds-11-raw bucket."
  role_arn                        = aws_iam_role.role.arn
  timeout                         = 15
  max_capacity                    = 0.0625
  command {
    name                          = "pythonshell"
    script_location               = "s3://${local.artifacts_bucket_name}/artifacts/glue_job_${local.datasource}/code/${local.script_name}.py"
    python_version                = 3.9
  }
  security_configuration          = "dlk-glue-sec-config"
  default_arguments = {
    "library-set"                 = "analytics"
    "--additional-python-modules" = "paramiko,jq,tabulate"
    # "--bucket_name"             = "${var.raw_bucket_name}"
    # "--enable-continuous-cloudwatch-log"  = false
    "--enable-glue-datacatalog"   = true
    # "--enable-metrics"          = false
    # "--enable-spark-ui"         = false
    # "--enable-job-insights"     = false
    "--environment"               = "sbx"
    "--extra-files"               = "s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/config.py,s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/common_functions.py,s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/gzip_s3_and_json_py3.py"
    # "--region"                  = "eu-west-1"
    "--job-bookmark-option"       = "job-bookmark-disable"
    "--job-language"              = "python"
    "--TempDir"                   = "s3://stg-dlk-sbx-glue-job-temporary-files/temporary/"
  }
  tags = {
    Author                        = "davide.moraschi@toptal.com"
    # ManagedBy                   = "Terraform"
    Project                       = "stg-dlk"
  }
}

# Add a SNS topic for notifications about GLue Workflow failures
resource "aws_sns_topic" "failure_topic" {
    name = "ds${var.datasource_number}-failure-topic"
}

resource "aws_sns_topic_subscription" "failure_email" {
  topic_arn = aws_sns_topic.failure_topic.arn
  protocol  = "email"  
  endpoint  = "davide.moraschi@straumann.com"
}
