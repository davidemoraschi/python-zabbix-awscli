data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# Define the provider and AWS region
provider "aws" {
  region  = "eu-west-1"
  profile = "816247855850_AdministratorAccess"
}

variable "datasource_number" {
  type    = string
  default = "14"
}

locals {
  datasource                = "ds${var.datasource_number}"
  # ext_bucket_name         = "stg-dlk-sbx-ds-${var.datasource_number}-ext"
  raw_bucket_name           = "stg-dlk-sbx-ds-${var.datasource_number}-raw"
  refined_bucket_name       = "stg-dlk-sbx-ds-${var.datasource_number}-refined"
  datasource_bucket_folder  = "events_feed/events_jsonl_gzip/"
  artifacts_bucket_name     = "stg-dlk-sbx-code-artifacts"
  raw_database_name         = "stg-dlk-sbx-ds${var.datasource_number}-raw-db"
  raw_role_name             = "stg-dlk-sbx-ds${var.datasource_number}-source-to-raw-glue-job-role"
  raw_script_name           = "stg-dlk-sbx-ds${var.datasource_number}-job-source-to-raw"
  refined_database_name     = "stg-dlk-sbx-ds${var.datasource_number}-refined-db"
  refined_role_name         = "stg-dlk-sbx-ds${var.datasource_number}-raw-to-refined-glue-job-role"
  refined_script_name       = "stg-dlk-sbx-ds${var.datasource_number}-job-raw-to-refined"
  kms_key_arn               = "arn:aws:kms:eu-west-1:816247855850:key/396cd8ff-4b3d-4b17-9df4-9449185fdd2e"
  ext_user_name             = "ds${var.datasource_number}_sap_cdp_ext_user"
  # ext_role_name           = "ds${var.datasource_number}_sap_cdp_ext_role"
}

# ===========================================================================================================================
# Raw zone
# ===========================================================================================================================
resource "aws_s3_bucket" "raw_bucket" {
  bucket              = local.raw_bucket_name
  force_destroy       = true
  object_lock_enabled = false
}

resource "aws_s3_bucket_policy" "raw_bucket_policy" {
  bucket = aws_s3_bucket.raw_bucket.id
  policy  = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/bucket-policy.json", { resource-arn = aws_s3_bucket.raw_bucket.arn })
}

resource "aws_s3_bucket_public_access_block" "raw_bucket_access_block" {
  bucket                  = aws_s3_bucket.raw_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "raw_bucket_versioning" {
  bucket = aws_s3_bucket.raw_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "raw_bucket_encryption" {
  bucket = aws_s3_bucket.raw_bucket.id  
  rule {
    bucket_key_enabled = true
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "raw_bucket_lifecycle" {
  bucket = aws_s3_bucket.raw_bucket.id 
  rule {
    id = "expire-after-365-days"
    filter {}
    expiration {
      days = 365
    }
    status = "Enabled"
  }
}

# resource "aws_cloudtrail" "raw_bucket_cloudtrail" {
#   depends_on = [aws_s3_bucket_policy.bucket_policy]
#   name                          = "${local.raw_bucket_name}_cloudtrail"
#   s3_bucket_name                = aws_s3_bucket.raw_bucket.id
#   include_global_service_events = false
#     event_selector {
#     read_write_type           = "All"
#     include_management_events = true
#     data_resource {
#       type   = "AWS::S3::Object"
#       values = ["arn:aws:s3:::${local.raw_bucket_name}/*"]
#     }
#   }
# }

resource "aws_iam_user" "ext_user" {
  name        = local.ext_user_name
}

resource "aws_iam_policy" "ext_user_policy" {
  name        = "${local.ext_user_name}_policy"
  policy      = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/user-policy.json", 
    { resource-arn = aws_s3_bucket.raw_bucket.arn })
}

resource "aws_iam_user_policy_attachment" "ext_user_policy_attachment" {
  user        = aws_iam_user.ext_user.name
  policy_arn  = aws_iam_policy.ext_user_policy.arn
}

resource "aws_iam_role" "raw_job_role" {
  name               = local.raw_role_name
  assume_role_policy = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/trust-policy.json", 
    { service = "glue.amazonaws.com" })
}

resource "aws_iam_policy" "raw_job_role_policy" {
  name = "${local.raw_role_name}_policy"
  policy = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/glue-role-policy.json", {  
    account_id          = data.aws_caller_identity.current.account_id
    region              = data.aws_region.current.name
    resource-arn        = aws_s3_bucket.raw_bucket.arn
    # ext-resource-arn  = "arn:aws:s3:::${local.ext_bucket_name}"
    raw_db_name         = local.raw_database_name
    refined_db_name     = local.refined_database_name
    failure_topic_name  = "ds${var.datasource_number}-failure-topic"
  kms_key_arn = local.kms_key_arn })
}

resource "aws_iam_role_policy_attachment" "raw_job_role_policy_attachment" {
  role       = aws_iam_role.raw_job_role.name
  policy_arn = aws_iam_policy.raw_job_role_policy.arn
}

resource "aws_lakeformation_resource" "raw_data_location" {
  arn      = aws_s3_bucket.raw_bucket.arn
  role_arn = aws_iam_role.raw_job_role.arn
}

resource "aws_glue_catalog_database" "raw_glue_database" {
  name         = local.raw_database_name
  description  = "Glue catalog db for ${local.datasource} raw zone."
  location_uri = "s3://${local.raw_bucket_name}"
}

resource "aws_lakeformation_permissions" "raw_database_permissions" {
  principal   = aws_iam_role.raw_job_role.arn
  permissions = ["CREATE_TABLE", "DESCRIBE"]
  database {
    name = aws_glue_catalog_database.raw_glue_database.name
  }
}

resource "aws_lakeformation_permissions" "raw_tables_permissions" {
  principal   = aws_iam_role.raw_job_role.arn
  permissions = ["ALL"]
  table {
    database_name = aws_glue_catalog_database.raw_glue_database.name
    wildcard      = true
  }
}

# resource "aws_glue_catalog_table" "page_views_jsonl_gzip" {
#   name                            = "page_views_jsonl_gzip"
#   database_name                   = aws_glue_catalog_database.raw_glue_database.name
#   table_type                      = "EXTERNAL_TABLE"
#   parameters                      = { "EXTERNAL" = "TRUE" }
#   storage_descriptor {
#     location                      = "s3://${local.raw_bucket_name}/${local.datasource_bucket_folder}PAGE_VIEW/"
#     input_format                  = "org.apache.hadoop.mapred.TextInputFormat"
#     output_format                 = "org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat"
#     ser_de_info {
#       name                        = "json_serde"
#       serialization_library       = "org.openx.data.jsonserde.JsonSerDe"
#       parameters                  = { "paths" = "contactid,eventtype,eventattributes" }
#     }
#       columns {
#         name = "contactid"
#         type = "string"
#       }
#       columns {
#         name = "eventtype"
#         type = "string"
#       }
#       columns {
#         name = "eventattributes"
#         type = "string"
#       }
#   }
# }

# resource "aws_glue_catalog_table" "biomaterial_state_updates_jsonl_gzip" {
#   name                            = "biomaterial_state_updates_jsonl_gzip"
#   database_name                   = aws_glue_catalog_database.raw_glue_database.name
#   table_type                      = "EXTERNAL_TABLE"
#   parameters                      = { "EXTERNAL" = "TRUE" }
#   storage_descriptor {
#     location                      = "s3://${local.raw_bucket_name}/${local.datasource_bucket_folder}BIOMATERIAL_STATE_UPDATE/"
#     input_format                  = "org.apache.hadoop.mapred.TextInputFormat"
#     output_format =               "org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat"
#     ser_de_info {
#       name                        = "json_serde"
#       serialization_library       = "org.openx.data.jsonserde.JsonSerDe"
#       parameters                  = { "paths" = "contactid,eventtype,eventattributes" }
#     }
#       columns {
#         name = "contactid"
#         type = "string"
#       }
#       columns {
#         name = "eventtype"
#         type = "string"
#       }
#       columns {
#         name = "eventattributes"
#         type = "string"
#       }
#   }
# }

# resource "aws_glue_catalog_table" "biomaterial_milestone_updates_jsonl_gzip" {
#   name                            = "biomaterial_milestone_updates_jsonl_gzip"
#   database_name                   = aws_glue_catalog_database.raw_glue_database.name
#   table_type                      = "EXTERNAL_TABLE"
#   parameters                      = { "EXTERNAL" = "TRUE" }
#   storage_descriptor {
#     location                      = "s3://${local.raw_bucket_name}/${local.datasource_bucket_folder}BIOMATERIAL_MILESTONE_UPDATE/"
#     input_format                  = "org.apache.hadoop.mapred.TextInputFormat"
#     output_format                 = "org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat"
#     ser_de_info {
#       name                        = "json_serde"
#       serialization_library       = "org.openx.data.jsonserde.JsonSerDe"
#       parameters                  = { "paths" = "contactid,eventtype,eventattributes" }
#     }
#       columns {
#         name = "contactid"
#         type = "string"
#       }
#       columns {
#         name = "eventtype"
#         type = "string"
#       }
#       columns {
#         name = "eventattributes"
#         type = "string"
#       }
#   }
# }

resource "aws_s3_object" "raw_glue_job_script" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/${local.raw_script_name}.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/${local.raw_script_name}.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/${local.raw_script_name}.py")
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

resource "aws_glue_job" "raw_glue_job" {
  name                            = local.raw_script_name
  description                     = "Part 1 of SAP CDP. Strips the outer array from the JSON and uploads it to the stg-dlk-sbx-ds-11-raw bucket."
  role_arn                        = aws_iam_role.raw_job_role.arn
  timeout                         = 15
  max_capacity                    = 0.0625
  command {
    name                          = "pythonshell"
    script_location               = "s3://${local.artifacts_bucket_name}/artifacts/glue_job_${local.datasource}/code/${local.raw_script_name}.py"
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
    "--WORKFLOW_NAME"             = "no_workflow"
    "--WORKFLOW_RUN_ID"           = "0"
    "--EVENT_TYPES"               = "[\"PAGE_VIEW\",\"BIOMATERIAL_STATE_UPDATE\",\"BIOMATERIAL_MILESTONE_UPDATE\"]"
    "--TempDir"                   = "s3://stg-dlk-sbx-glue-job-temporary-files/temporary/"
  }
  tags = {
    Author                        = "davide.moraschi@toptal.com"
    # ManagedBy                   = "Terraform"
    Project                       = "stg-dlk"
  }
}

# Workflow may not be the best approach for running the same job multiple times with parameters,
# but Step Funcions are a bad beast to debug. Eventually it is better to use a loop inside the Glue Job
# and pass the event types in an array
 
resource "aws_glue_workflow" "pipeline" {
  name = "ds${var.datasource_number}_pipeline"
  max_concurrent_runs = 1
}

resource "aws_glue_trigger" "source_to_raw_pipeline_trigger" {
  name                  = "ds${var.datasource_number}_pipeline_schedule"
  schedule              = "cron(0 4 ? * MON-FRI *)"  #cron(Minutes Hours Day-of-month Month Day-of-week Year)
  type                  = "SCHEDULED"
  workflow_name         = aws_glue_workflow.pipeline.name
  actions {
    job_name            = aws_glue_job.raw_glue_job.name
    timeout             = 15  
    arguments           = {
        "--EVENT_TYPES" = "[\"PAGE_VIEW\",\"BIOMATERIAL_STATE_UPDATE\",\"BIOMATERIAL_MILESTONE_UPDATE\"]"}
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

# ===========================================================================================================================
# Refined zone
# ===========================================================================================================================
resource "aws_s3_bucket" "refined_bucket" {
  bucket              = local.refined_bucket_name
  force_destroy       = true
  object_lock_enabled = false
}

resource "aws_s3_bucket_policy" "refined_bucket_policy" {
  bucket = aws_s3_bucket.refined_bucket.id
  policy  = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/bucket-policy.json", 
    { resource-arn = aws_s3_bucket.refined_bucket.arn })
}

resource "aws_s3_bucket_public_access_block" "refined_bucket_access_block" {
  bucket                  = aws_s3_bucket.refined_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "refined_bucket_encryption" {
  bucket = aws_s3_bucket.refined_bucket.id  
  rule {
    bucket_key_enabled = true
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_iam_role" "refined_job_role" {
  name               = local.refined_role_name
  assume_role_policy = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/trust-policy.json", 
    { service = "glue.amazonaws.com" })
}

resource "aws_iam_policy" "refined_job_role_policy" {
  name = "${local.refined_role_name}_policy"
  policy = templatefile("${path.module}/artifacts/ds${var.datasource_number}/glue/policies/glue-role-policy.json", {  
    account_id          = data.aws_caller_identity.current.account_id
    region              = data.aws_region.current.name
    resource-arn        = aws_s3_bucket.refined_bucket.arn
    # ext-resource-arn  = "arn:aws:s3:::${local.ext_bucket_name}"
    raw_db_name         = local.raw_database_name
    refined_db_name     = local.refined_database_name
    failure_topic_name  = "ds${var.datasource_number}-failure-topic"
  kms_key_arn = local.kms_key_arn })
}

resource "aws_iam_role_policy_attachment" "refined_job_role_policy_attachment" {
  role       = aws_iam_role.refined_job_role.name
  policy_arn = aws_iam_policy.refined_job_role_policy.arn
}

resource "aws_lakeformation_resource" "refined_data_location" {
  arn      = aws_s3_bucket.refined_bucket.arn
  role_arn = aws_iam_role.refined_job_role.arn
}

resource "aws_glue_catalog_database" "refined_glue_database" {
  name         = local.refined_database_name
  description  = "Glue catalog db for ${local.datasource} refined zone."
  location_uri = "s3://${local.refined_bucket_name}"
}

resource "aws_lakeformation_permissions" "refined_database_permissions" {
  principal   = aws_iam_role.refined_job_role.arn
  permissions = ["CREATE_TABLE", "DESCRIBE"]
  database {
    name = aws_glue_catalog_database.refined_glue_database.name
  }
}

resource "aws_lakeformation_permissions" "refined_tables_permissions" {
  principal   = aws_iam_role.refined_job_role.arn
  permissions = ["ALL"]
  table {
    database_name = aws_glue_catalog_database.refined_glue_database.name
    wildcard      = true
  }
}

resource "aws_lakeformation_permissions" "raw_refined_database_permissions" {
  principal   = aws_iam_role.refined_job_role.arn
  permissions = ["CREATE_TABLE", "DESCRIBE"]
  database {
    name = aws_glue_catalog_database.raw_glue_database.name
  }
}

resource "aws_lakeformation_permissions" "raw_refined_tables_permissions" {
  principal   = aws_iam_role.refined_job_role.arn
  permissions = ["ALL"]
  table {
    database_name = aws_glue_catalog_database.raw_glue_database.name
    wildcard      = true
  }
}

resource "aws_s3_object" "refiend_glue_job_script" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/code/${local.refined_script_name}.py"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/code/${local.refined_script_name}.py"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/code/${local.refined_script_name}.py")
}

resource "aws_s3_object" "sql_job_script_001" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/sql/001. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_page_views_jsonl_gzip.sql"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/sql/001. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_page_views_jsonl_gzip.sql"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/sql/001. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_page_views_jsonl_gzip.sql")
}

resource "aws_s3_object" "sql_job_script_002" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/sql/002. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_biomaterial_milestone_updates_jsonl_gzip.sql"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/sql/002. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_biomaterial_milestone_updates_jsonl_gzip.sql"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/sql/002. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_biomaterial_milestone_updates_jsonl_gzip.sql")
}

resource "aws_s3_object" "sql_job_script_003" {
  bucket      = local.artifacts_bucket_name
  key         = "artifacts/glue_job_${local.datasource}/sql/003. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_biomaterial_state_updates_jsonl_gzip.sql"
  source      = "${path.module}/artifacts/ds${var.datasource_number}/glue/sql/003. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_biomaterial_state_updates_jsonl_gzip.sql"
  source_hash = filemd5("${path.module}/artifacts/ds${var.datasource_number}/glue/sql/003. CREATE EXTERNAL TABLE stg-dlk-sbx-ds14-raw-db.sapcdp_biomaterial_state_updates_jsonl_gzip.sql")
}

resource "aws_glue_job" "refined_glue_job" {
  name                            = local.refined_script_name
  description                     = "Part 2 of SAP CDP. Runs SQL transformations on refined database."
  role_arn                        = aws_iam_role.refined_job_role.arn
  timeout                         = 15
  max_capacity                    = 0.0625
  command {
    name                          = "pythonshell"
    script_location               = "s3://${local.artifacts_bucket_name}/artifacts/glue_job_${local.datasource}/code/${local.refined_script_name}.py"
    python_version                = 3.9
  }
  security_configuration          = "dlk-glue-sec-config"
  default_arguments = {
    "library-set"                 = "analytics"
    "--additional-python-modules" = "paramiko,jq,tabulate"
    # "--bucket_name"             = "${var.refined_bucket_name}"
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
    "--WORKFLOW_NAME"             = "no_workflow"
    "--WORKFLOW_RUN_ID"           = "0"
    # "--EVENT_TYPES"               = "[\"PAGE_VIEW\",\"BIOMATERIAL_STATE_UPDATE\",\"BIOMATERIAL_MILESTONE_UPDATE\"]"
    "--TempDir"                   = "s3://stg-dlk-sbx-glue-job-temporary-files/temporary/"
  }
  tags = {
    Author                        = "davide.moraschi@toptal.com"
    # ManagedBy                   = "Terraform"
    Project                       = "stg-dlk"
  }
}

resource "aws_glue_trigger" "raw_to_refined_pipeline_trigger" {
  name                  = "ds${var.datasource_number}_raw_to_refined_trigger"
  type                  = "CONDITIONAL"
  workflow_name         = aws_glue_workflow.pipeline.name
  actions {
    job_name            = aws_glue_job.refined_glue_job.name
    timeout             = 15  
  }
  predicate {
    conditions {
      job_name = aws_glue_job.raw_glue_job.name
      state    = "SUCCEEDED"
    }
  }
}
