data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# Define the provider and AWS region
provider "aws" {
  region  = "eu-west-1"
  profile = "816247855850_AdministratorAccess"
}

variable "datasource_number" {
  type    = string
  default = "6"
}

locals {
  datasource               = "ds${var.datasource_number}"
  ext_bucket_name          = "stg-dlk-sbx-ds-${var.datasource_number}-ext"
  raw_bucket_name          = "stg-dlk-sbx-ds-${var.datasource_number}-raw"
  datasource_bucket_folder = "docebo_feed/reports_csv_gzip/"
  artifacts_bucket_name    = "stg-dlk-sbx-code-artifacts"
  database_name            = "stg-dlk-sbx-ds${var.datasource_number}-raw-db"
  role_name                = "stg-dlk-sbx-ds${var.datasource_number}-source-to-raw-glue-job-role-new-report"
  script_name              = "stg-dlk-sbx-ds${var.datasource_number}-job-source-to-raw-new-report"
  kms_key_arn              = "arn:aws:kms:eu-west-1:816247855850:key/396cd8ff-4b3d-4b17-9df4-9449185fdd2e"
  # glue_job_role_arn      = "arn:aws:iam::816247855850:role/stg-dlk-sbx-ds6-source-to-raw-glue-job-role"
  docebo_api_secret_name   = "stg/dlk/docebo/ds6/secrets"
}

# resource "aws_s3_bucket" "bucket" {
#   bucket              = local.raw_bucket_name
#   force_destroy       = true
#   object_lock_enabled = false
# }

# resource "aws_s3_bucket_public_access_block" "bucket_access_block" {
#   bucket                  = aws_s3_bucket.bucket.id
#   block_public_acls       = true
#   block_public_policy     = true
#   ignore_public_acls      = true
#   restrict_public_buckets = true
# }

resource "aws_iam_role" "job_role" {
  name               = local.role_name
  assume_role_policy = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/trust-policy.json", { service = "glue.amazonaws.com" })
}

resource "aws_iam_policy" "job_role_policy" {
  name = "${local.role_name}_policy"
  policy = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/glue-role-policy.json", {  
    account_id              = data.aws_caller_identity.current.account_id
    region                  = data.aws_region.current.name
    resource-arn            = "arn:aws:s3:::stg-dlk-sbx-ds-6-raw" # was: aws_s3_bucket.bucket.arn
    ext-resource-arn        = "arn:aws:s3:::${local.ext_bucket_name}"
    raw_db_name             = local.database_name
    refined_db_name         = "stg-dlk-sbx-ds${var.datasource_number}-refined-db"
    kms_key_arn             = local.kms_key_arn 
    docebo_api_secret_name  = local.docebo_api_secret_name
    failure_topic_name      = "ds${var.datasource_number}-failure-topic"
  })
}

resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  role       = aws_iam_role.job_role.name
  policy_arn = aws_iam_policy.job_role_policy.arn
}

# resource "aws_lakeformation_resource" "data_location" {
#   arn      = aws_s3_bucket.bucket.arn
#   role_arn = aws_iam_role.role.arn
# }

# resource "aws_glue_catalog_database" "glue_database" {
#   name         = local.database_name
#   description  = "Glue catalog db for ${local.datasource} raw zone."
#   location_uri = "s3://${local.raw_bucket_name}"
# }

# resource "aws_lakeformation_permissions" "database_permissions" {
#   principal   = aws_iam_role.role.arn
#   permissions = ["CREATE_TABLE", "DESCRIBE"]
#   database {
#     name = aws_glue_catalog_database.glue_database.name
#   }
# }

# resource "aws_lakeformation_permissions" "tables_permissions" {
#   principal   = aws_iam_role.role.arn
#   permissions = ["ALL"]
#   table {
#     database_name = aws_glue_catalog_database.glue_database.name
#     wildcard      = true
#   }
# }

resource "aws_glue_catalog_table" "users_csv_gzip" {
  name                      = "users_csv_gzip"
  database_name             = local.database_name
  table_type                = "EXTERNAL_TABLE"
  parameters                = { "EXTERNAL" = "TRUE" }
  storage_descriptor {
    location                = "s3://${local.raw_bucket_name}/${local.datasource_bucket_folder}"
    input_format            = "org.apache.hadoop.mapred.TextInputFormat"
    output_format           = "org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat"
    ser_de_info {
      name                  = "OpenCSVSerde"
      serialization_library = "org.apache.hadoop.hive.serde2.OpenCSVSerde"
      parameters            = { "paths" = "username,branchname,branchpath,branchescodes" }
    }
    columns {
      name                  = "username"
      type                  = "string"
    }
    columns {
      name                  = "branchname"
      type                  = "string"
    }
    columns {
      name                  = "branchpath"
      type                  = "string"
    }
    columns {
      name                  = "branchescodes"
      type                  = "string"
    }
  }
}

resource "aws_s3_object" "glue_job_script" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/${local.script_name}.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/${local.script_name}.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/${local.script_name}.py")
}

resource "aws_s3_object" "glue_job_config" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/config.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/config.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/config.py")
}

resource "aws_s3_object" "glue_job_common_functions" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/common_functions.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/common_functions.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/common_functions.py")
}

resource "aws_s3_object" "glue_job_gzip_s3_and_json" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/gzip_s3_and_json_py3.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/gzip_s3_and_json_py3.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/gzip_s3_and_json_py3.py")
}

resource "aws_s3_object" "glue_job_token_manager" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/TokenManager.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/TokenManager.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/TokenManager.py")
}

resource "aws_glue_job" "glue_job" {
  name                                   = local.script_name
  description                            = "Part 1 of Docebo - Retrieves the CSV reports and uploads them to the stg-dlk-sbx-ds-6-raw bucket."
  role_arn                               = aws_iam_role.job_role.arn
  timeout                                = 15
  max_capacity                           = 0.0625
  command {
    name                                 = "pythonshell"
    script_location                      = "s3://${local.artifacts_bucket_name}/artifacts/glue_job_${local.datasource}/code/${local.script_name}.py"
    python_version                       = 3.9
  }
  security_configuration                 = "dlk-glue-sec-config"
  default_arguments = {
    "library-set"                        = "analytics"
    "--additional-python-modules"        = "paramiko,jq,tabulate"
    # "--bucket_name"                    = "${var.raw_bucket_name}"
    "--enable-continuous-cloudwatch-log" = false
    "--enable-glue-datacatalog"          = true
    "--enable-metrics"                   = false
    "--enable-spark-ui"                  = false
    "--enable-job-insights"              = false
    "--environment"                      = "sbx"
    "--extra-files"                      = "s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/TokenManager.py,s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/config.py,s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/common_functions.py,s3://stg-dlk-sbx-code-artifacts/artifacts/glue_job_${local.datasource}/code/gzip_s3_and_json_py3.py"
    # "--region"                         = "eu-west-1"
    "--job-bookmark-option"              = "job-bookmark-disable"
    "--job-language"                     = "python"
    "--WORKFLOW_NAME"                    = "no_workflow"
    "--WORKFLOW_RUN_ID"                  = "0"
    "--REPORT_IDS"                       = "[\"10e865fe-75d1-49a5-bec4-b0db905023e4\",\"b7736e69-6a11-4f16-bca2-49b863ba4670\"]"
    "--TempDir"                          = "s3://stg-dlk-sbx-glue-job-temporary-files/temporary/"
  }
  tags = {
    Author                               = "davide.moraschi@toptal.com"
    # ManagedBy                          = "Terraform"
    Project                              = "stg-dlk"
  }
}

# Workflow may not be the best approach for running the same job multiple times with parameters,
# but Step Funcions are a bad beast to debug. Eventually it is better to use a loop inside the Glue Job
# and pass the report ids in an array

resource "aws_glue_workflow" "pipeline" {
  name = "ds${var.datasource_number}_pipeline"
  max_concurrent_runs = 1
}

resource "aws_glue_trigger" "pipeline_trigger" {
  name                  = "ds${var.datasource_number}_pipeline_schedule"
  schedule              = "cron(0 3 ? * MON-FRI *)"  #cron(Minutes Hours Day-of-month Month Day-of-week Year)
  type                  = "SCHEDULED"
  workflow_name         = aws_glue_workflow.pipeline.name
  actions {
    job_name            = aws_glue_job.glue_job.name
    timeout             = 15  
    arguments           = {
        "--REPORT_IDS"  = "[\"7dd3a445-b55c-40d6-9293-cf767c4b7c85\",\"e0c33c01-9b3d-4e57-8c6f-e2f5aff29e7f\",\"d943fa1b-a420-4082-82e4-164721a3a4f9\",\"87ef3e0e-6f66-4256-a294-4858bafddb66\",\"836d478a-2839-4f1e-b75f-31682618ec8b\",\"0f2cce31-8ba5-44d4-b73f-b1b4589c74ed\",\"5f895d7d-7a3f-4de2-8cfb-a871d2b8780c\",\"8605e47a-0238-4049-879a-d95f2d40dd62\",\"b7736e69-6a11-4f16-bca2-49b863ba4670\"]"}
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
