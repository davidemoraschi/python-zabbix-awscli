### input variables for glue catalog database
# variable "datalake_zone" {
#   type    = list(string)
#   description = "datalake zones: raw, refined, curated"
#   default = ["raw", "refined"] # "curated"
# }

variable "kms_key_arn" {
  description = "External kms key to use for dlk"
  default = null
}

variable "datalake_zone" {
  type    = map(string)
  description = "datalake zones: raw, refined, curated"
  default = {
    zone_raw = "raw" 
    zone_refined = "refined"
    # zone_curated = "curated"
  }
}

variable "create_glue_catalog_db" {
  description = "Whether to create catalog database"
  type = bool
  default = true
}

variable "glue_catalog_db_name" {
  type        = string
  description = "Required. Glue catalog database name. Glue database where results are written. Acceptable characters are lowercase letters, numbers, and the underscore character."
  default = ""
}

variable "glue_catalog_db_description" {
  type        = string
  description = "Optional. Glue catalog database description."
  default     = null
}

variable "glue_catalog_id" {
  type        = string
  description = "Optional. ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID."
  default     = null
}

variable "glue_location_uri" {
  type        = string
  description = "Optional. Location of the database (for example, an HDFS path)."
  default     = null
}

variable "glue_db_parameters" {
  type        = map(string)
  description = "Optional. Map of key-value pairs that define parameters and properties of the database."
  default     = null
}

variable "create_table_default_permission" {
  # With `type = any` , fields `null` will be not used
  type        = any
  description = "Creates a set of default permissions on the table for principals."
  default     = null
}

variable "target_database" {
  type = object({
    # If `target_database` is provided (not `null`), all these fields are required
    glue_catalog_id    = string
    glue_catalog_db_name = string
  })
  description = " Configuration block for a target database for resource linking."
  default     = null
}

### input variables glue catalog tables
# variable "create_glue_catalog_table" {
#   description = "Whether to create catalog table"
#   type = bool
#   default = false
# }


# variable "glue_catalog_table_name" {
#   type = string
#   description = "(Required) Name of the table."
# }

# variable "glue_catalog_table_type" {
#   type = string
#   description = "Type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.). While optional, some Athena DDL queries such as ALTER TABLE and SHOW CREATE TABLE will fail if this argument is empty."
# }
 
# variable "glue_catalog_table_parameters" {
#   type = map(string)
#   description = "Properties associated with this table."
# }


### input variables glue crawler

variable "create_glue_crawler" {
  description = "Whether to create glue crawler"
  type = bool
  default = true
}

variable "glue_crawler_name" {
  type        = string
  description = "Required. Glue crawler name. If not provided, the name will be generated from the context."
  default     = null
}

variable "glue_crawler_description" {
  type        = string
  description = "Glue crawler description."
  default     = null
}

variable "glue_crawler_role" {
  type        = string
  description = "Required. Crawler role to be attached to the instance. The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources."
  default = ""
}

variable "glue_crawler_schedule" {
  type = string
  description = "A cron expression to specify the schedule. Use Time-Based Schedules for Jobs and Crawlers. For example, to run it every day at 05:00 UTC, specify: cron(00 05 * * ? *)."
  default = null
}


variable "glue_crawler_configuration" {
  type        = string
  description = "JSON string of configuration information."
  default     = null
}

variable "glue_crawler_classifiers" {
  type        = any
  description = "(Optional) List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification."
  default     = null
}

variable "glue_lake_formation_configuration" {
  type        = map(string)
  description = "The Lake Formation configuration settings for the crawler."
  default     = null
}

variable "glue_security_configuration" {
  type        = string
  description = "The name of Security Configuration to be used by the crawler."
  default     = null
}

variable "glue_table_prefix" {
  type        = string
  description = "The table prefix used for catalog tables that are created."
  default     = null
}

variable "s3_target" {
  type        = list(any)
  description = "List of nested Amazon S3 target arguments."
  /*  
  path                = string (REQUIRED)
  connection_name     = string
  exclusions          = list(string)
  sample_size         = number
  event_queue_arn     = string
  dlq_event_queue_arn = string
  */
  default     = null
}

variable "glue_catalog_target" {
  type = list(object({
    glue_catalog_db_name = string
    tables        = list(string)
  }))
  description = "List of nested Glue catalog target arguments. (Required) database_name(glue_catalog_db_name) : name of the Glue database // tables: a list of catalog tables to be synchronized."
  default     = null
}

variable "schema_change_policy" {
  type        = map(string)
  description = "delete_behavior: when the crawler finds a deleted object. Valid values: LOG, DELETE_FROM_DATABASE, or DEPRECATE_IN_DATABASE. Defaults to DEPRECATE_IN_DATABASE. // update_behavior - when the crawler finds a changed schema. Valid values: LOG or UPDATE_IN_DATABASE. Defaults to UPDATE_IN_DATABASE."
  default = {
    "delete_behavior" = "DEPRECATE_IN_DATABASE"
    "update_behavior" = "UPDATE_IN_DATABASE"
  }
}

variable "recrawl_policy" {
  type        = map(string)
  description = "Specifies whether to crawl the entire dataset again, crawl only folders that were added since the last crawler run, or crawl what S3 notifies the crawler of via SQS. Valid Values are: CRAWL_EVENT_MODE, CRAWL_EVERYTHING and CRAWL_NEW_FOLDERS_ONLY. Default value is CRAWL_EVERYTHING"
  default = {
    "recrawl_behavior" = "CRAWL_EVERYTHING"
  }
}

### glue_job 
variable "create_glue_job" {
  description = "Whether to create glue job"
  type = bool
  default = false
}

variable "glue_job_name" {
  type        = string
  description = "Required. The name you assign to this job. It must be unique in your account. If not provided, the name will be generated from the context."
  default     = null
}

variable "glue_job_role_arn" {
  type        = string
  description = "Required. The ARN of the IAM role associated with this job."
  default = ""
}

variable "glue_job_description" {
  type        = string
  description = "Glue job description."
  default     = null
}

variable "glue_job_connections" {
  type        = list(string)
  description = "The list of connections used for this job."
  default     = null
}

variable "glue_job_default_arguments" {
  type        = map(string)
  description = "The map of default arguments for the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes."
  default     = null
}

variable "glue_job_non_overridable_arguments" {
  type        = map(string)
  description = "Non-overridable arguments for this job, specified as name-value pairs."
  default     = null
}

variable "glue_version" {
  type        = string
  description = "The version of Glue to use. Currently from 2.0 to 4.0. We chose v.3"
  default     = "2.0"
}

variable "glue_job_timeout" {
  type        = number
  description = "The job timeout in minutes. The default is 2880 minutes (48 hours) for `glueetl` and `pythonshell` jobs, and `null` (unlimited) for `gluestreaming` jobs."
  default     = 2880
}

variable "glue_job_number_of_workers" {
  type        = number
  description = "The number of workers of a defined `worker_type` that are allocated when a job runs."
  default     = null
}

variable "glue_job_worker_type" {
  type        = string
  description = "The type of predefined worker that is allocated when a job runs. Accepts a value of `Standard`, `G.1X`, or `G.2X`."
  default     = null
}

variable "glue_job_max_capacity" {
  type        = number
  description = "The maximum number of AWS Glue data processing units (DPUs) that can be allocated when the job runs. Required when `pythonshell` is set, accept either 0.0625 or 1.0. Use `number_of_workers` and `worker_type` arguments instead with `glue_version` 2.0 and above."
  default     = null
}

variable "glue_job_security_configuration" {
  type        = string
  description = "The name of the Security Configuration to be associated with the job."
  default     = null
}

variable "glue_job_max_retries" {
  type        = number
  description = " The maximum number of times to retry the job if it fails."
  default     = null
}

variable "glue_job_command" {
  type        = map(any)
  description = /* 
  Required. Some fields are optional, not specified set to 'null'. 
  - command name of the job: name = string (default = "glueetl")
  - specifies the S3 path to a script that executes the job: script_location = string (required)
  - Python version 2/3 being used to execute a Python shell job: python_version = number. "*/""
  default = {}
}

variable "glue_job_notification_property" {
  type = object({
    notify_delay_after = number
  })
  description = "Notification property of the job. After a job run starts, the amount of minutes to wait before sending a job run delay notification."
  default     = null
}

variable "glue_job_execution_property" {
  type = object({
    max_concurrent_runs = number
  })
  description = "Execution property of the job. The maximum amount of concurrent runs allowed for the job. The default is 1."
  default     = {max_concurrent_runs = 1}
}

## glue_trigger
variable "create_glue_trigger" {
  description = "Whether to create glue trigger"
  type = bool
  default = false
}

variable "glue_trigger_name" {
  description = "(Required) Name of the trigger"
  type = string
  default = ""
}

variable "glue_trigger_type" {
  description = "(Required) The type of trigger. Valid values are CONDITIONAL, EVENT, ON_DEMAND, and SCHEDULED."
  type = string
  default = ""
}

variable "glue_trigger_schedule" {
  description = "(Required) for the trigger_type SCHEDULED. Cron formatted schedule."
  type = string
  default = null
}

variable "glue_trigger_enabled" {
  type        = bool
  description = "Whether to start the created trigger."
  default     = false
}

variable "glue_trigger_start_on_creation" {
  type        = bool
  description = "Set to true to start SCHEDULED and CONDITIONAL triggers when created. True is not supported for ON_DEMAND triggers."
  default     = false
}

variable "glue_trigger_predicate" {
  #  Conditions for activating the trigger. Required for triggers where type is `CONDITIONAL`.
  #  type = object({
  #    # How to handle multiple conditions. Defaults to `AND`. Valid values are `AND` or `ANY`
  #    logical = string
  #    conditions = list(object({
  #      job_name         = string
  #      crawler_name     = string
  #      state            = string
  #      crawl_state      = string
  #      logical_operator = string
  #    }))
  #  })
  # Using `type = any` since some of the the fields are optional
  type        = any
  description = "A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`."
  default     = null
}

variable "glue_trigger_actions" {
  description = "(Required) List of actions initiated by this trigger when it fires."
  type = map(any)
  default = {}
}

variable "glue_trigger_event_batching_condition" {
  #  type = object({
  #    batch_size   = number
  #    batch_window = number
  #  })

  # Using `type = map(number)` since some of the the fields are optional and we don't want to force the caller to specify all of them and set to `null` those not used
  type        = map(number)
  description = "Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires."
  default     = null
}

variable "create_glue_connection" {
  description = "Whether to create glue connection"
  type = bool
  default = false
}

variable "glue_connector_name" {
  description = "Name of the glue connector"
  type        = string
  default     = null
}

variable "glue_connection_description" {
  description = "Name of the glue connector"
  type        = string
  default     = null
}

variable "glue_connection_type" {
  description = "The type of the connection. Supported are: JDBC, MONGODB, KAFKA, and NETWORK. Defaults to JBDC"
  type        = string
  default     = null
}

variable "glue_connection_properties" {
  type        = map(string)
  description = "A map of key-value pairs used as parameters for this connection."
  default     = null
}

variable "glue_match_criteria" {
  type        = list(string)
  description = "A list of criteria that can be used in selecting this connection."
  default     = null
}

variable "glue_connection_network" {
  description = "List of network requirements for the glue connection."
  type = any
  default = {}
}


### tags
variable "tags" {
  description = "A map of tags to add to all resources"
  type        = map(string)
  default     = {}
}
