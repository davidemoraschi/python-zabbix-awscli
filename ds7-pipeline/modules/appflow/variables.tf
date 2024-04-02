variable "name" {
  description = " Name of the connector profile. The name is unique for each ConnectorProfile in your AWS account."
  type        = string
  default     = ""
}

variable "connection_mode" {
  description = " Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet. One of: Public, Private."
  type        = string
  default     = "Private"
}

variable "connector_type" {
  description = "The type of connector. One of: Amplitude, CustomConnector, CustomerProfiles, Datadog, Dynatrace, EventBridge, Googleanalytics, Honeycode, Infornexus, LookoutMetrics, Marketo, Redshift, S3, Salesforce, SAPOData, Servicenow, Singular, Slack, Snowflake, Trendmicro, Upsolver, Veeva, Zendesk."
  type        = string
  default     = ""
}

variable "kms_arn" {
  description = "ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key."
  type        = string
}

variable "connector_profile_credentials" {
  description = "The connector-specific credentials required by each connector."
  type        = map(string)
  default     = null

}
variable "connector_profile_properties" {
  description = "The connector-specific properties of the profile configuration."
  type        = map(string)
  default     = null

}
variable "create_appflow" {
  description = "Boolean to specify whether to create an appflow"
  type        = bool
  default     = false
}
variable "tags" {
  description = "A map of tags to use on all resources"
  type        = map(string)
  default     = {}
}
variable "cross_account_role" {
  type        = string
  description = "Cross account role"
  default     = ""
}
variable "appflow_map" {
  description = "Map of appflows and its properties"
  type = map(object({
    appflow_name           = string
    appflow_description    = optional(string)
    dest_conn_type         = string
    dest_bucket_name       = string
    src_conn_type          = string
    src_conn_obj_path      = string
    connector_profile_name = string
    s3_output_format_config = optional(object({
      aggregationConfig = optional(object({
        aggregationType = optional(string)
      }))
      fileType = optional(string)
      prefixConfig = optional(object({
        prefixFormat = optional(string)
        prefixType   = optional(string)
      }))
    }))
    ## Optional SAPOData parameters not supported by AWS Terraform module
    ## See https://docs.aws.amazon.com/cli/latest/reference/appflow/update-flow.html for parameter description
    ## To apply this parameters, it is needed to force a flow modificacion changing, for example, description field
    sapodata_aditional_params = optional(object({
      parallelismConfig = object({
        maxParallelism = number
      })
      paginationConfig = object({
        maxPageSize = number
      })
    }))
    flow_tasks = list(object({
      sourceFields = list(string),
      taskType     = string,
      connectorOperator = object({
        SAPOData = string
      }),
      destinationField = optional(string),
      taskProperties = optional(object({
        DESTINATION_DATA_TYPE = optional(string),
        SOURCE_DATA_TYPE      = optional(string),
        DATA_TYPE             = optional(string),
        VALUE                 = optional(string)
      }))
    }))
    trigger-config = object({
      triggerType = string
      triggerProperties = optional(object({
        Scheduled = optional(object({
          scheduleExpression = optional(string)
          dataPullMode       = optional(string)
          scheduleStartTime  = optional(string)
        }))
      }))
    })
    incremental-pull-config = optional(object({
      datetimeTypeFieldName = optional(string)
    }))
  }))
  default = {}
}
variable "dest_bucket_name" {
  description = "destination bucket name for the appflow"
  default     = ""
  type        = string
}

variable "appflow_glue_role_arn" {
  description = "IAM role for glue data integration"
  type        = string
  default     = ""
}
variable "appflow_glue_db_name" {
  description = "Glue database name for the appflow"
  type        = string
  default     = ""
}
variable "appflow_glue_table_prefix" {
  description = "Glue table prefix for appflow"
  type        = string
  default     = ""
}
