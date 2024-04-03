data "aws_region" "current" {}
data "aws_caller_identity" "current" {}# Define the provider and AWS region
provider "aws" {
  region  = "eu-west-1"
  profile = "816247855850_AdministratorAccess"
}

# import {
#   to = aws_appflow_flow.SAP_MKTCloud_AWSWEBREGFORM_CDS_Full
#   id = "arn:aws:appflow:eu-west-1:816247855850:flow/SAP_MKTCloud_AWSWEBREGFORM_CDS_Full"
# }

# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.

# __generated__ by Terraform from "arn:aws:appflow:eu-west-1:816247855850:flow/SAP_MKTCloud_AWSWEBREGFORM_CDS_Full"
resource "aws_appflow_flow" "SAP_MKTCloud_AWSWEBREGFORM_CDS_Full" {
  description = "SAP_MKTCloud_AWSWEBREGFORM_CDS_Full"
  kms_arn     = "arn:aws:kms:eu-west-1:816247855850:key/396cd8ff-4b3d-4b17-9df4-9449185fdd2e"
  name        = "SAP_MKTCloud_AWSWEBREGFORM_CDS_Full"
  tags = {
    ManagedBy = "Terraform"
    Project   = "stg-dlk"
  }
  tags_all = {
    ManagedBy = "Terraform"
    Project   = "stg-dlk"
  }
  destination_flow_config {
    api_version            = null
    connector_profile_name = null
    connector_type         = "S3"
    destination_connector_properties {
      s3 {
        bucket_name   = "stg-dlk-sbx-ds-7-raw"
        bucket_prefix = null
        s3_output_format_config {
          file_type                   = "PARQUET"
          preserve_source_data_typing = false
          aggregation_config {
            aggregation_type = "None"
            target_file_size = 0
          }
          prefix_config {
            prefix_format = "HOUR"
            prefix_type   = "PATH"
          }
        }
      }
    }
  }
  source_flow_config {
    api_version            = null
    connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
    connector_type         = "SAPOData"
    source_connector_properties {
      sapo_data {
        object_path = "/sap/opu/odata/sap/YY1_AWSWEBREGFORM_CDS/YY1_AWSWebRegForm"
      }
    }
  }
  task {
    destination_field = "CampaignID"
    source_fields     = ["CampaignID"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "ContentPageFormID"
    source_fields     = ["ContentPageFormID"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "ContentPageFormName"
    source_fields     = ["ContentPageFormName"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "EmailAddress"
    source_fields     = ["EmailAddress"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "FullName"
    source_fields     = ["FullName"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "Interaction"
    source_fields     = ["Interaction"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.Guid"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionContact"
    source_fields     = ["InteractionContact"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.Guid"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionContactId"
    source_fields     = ["InteractionContactId"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionContactOrigin"
    source_fields     = ["InteractionContactOrigin"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionSourceObject"
    source_fields     = ["InteractionSourceObject"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionStatus"
    source_fields     = ["InteractionStatus"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionTimeStampUTC"
    source_fields     = ["InteractionTimeStampUTC"]
    task_properties = {
      DESTINATION_DATA_TYPE = "timestamp"
      SOURCE_DATA_TYPE      = "datetime"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "InteractionType"
    source_fields     = ["InteractionType"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "MarketingArea"
    source_fields     = ["MarketingArea"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = "PhoneNumber"
    source_fields     = ["PhoneNumber"]
    task_properties = {
      DESTINATION_DATA_TYPE = "string"
      SOURCE_DATA_TYPE      = "Edm.String"
    }
    task_type = "Map"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "NO_OP"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  task {
    destination_field = null
    source_fields     = ["Interaction", "InteractionContactOrigin", "InteractionContactId", "InteractionType", "InteractionStatus", "InteractionTimeStampUTC", "CampaignID", "InteractionSourceObject", "MarketingArea", "ContentPageFormID", "ContentPageFormName", "FullName", "EmailAddress", "PhoneNumber", "InteractionContact"]
    task_properties   = {}
    task_type         = "Filter"
    connector_operator {
      amplitude        = null
      custom_connector = null
      datadog          = null
      dynatrace        = null
      google_analytics = null
      infor_nexus      = null
      marketo          = null
      s3               = null
      salesforce       = null
      sapo_data        = "PROJECTION"
      service_now      = null
      singular         = null
      slack            = null
      trendmicro       = null
      veeva            = null
      zendesk          = null
    }
  }
  trigger_config {
    trigger_type = "OnDemand"
    trigger_properties {
    }
  }
}
