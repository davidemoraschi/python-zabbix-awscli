data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# Define the provider and AWS region
provider "aws" {
  region  = "eu-west-1"
  profile = "816247855850_AdministratorAccess"
}

variable "datasource_number" {
  type    = string
  default = "7"
}

variable "env" {
  type        = string
  description = "the environment of deployment name"
  default = "sbx"
}

variable "external_kms_key_arn" {
  type        = string
  description = "External kms key to use for dlk"
  default = "arn:aws:kms:eu-west-1:816247855850:key/396cd8ff-4b3d-4b17-9df4-9449185fdd2e"
}

variable "cross_account_role" {
  type    = string
  default = "arn:aws:iam::816247855850:role/stg-dlk-devops"
}

locals {
  datasource            = "ds${var.datasource_number}"
  account_id            = data.aws_caller_identity.current.account_id
  region                = data.aws_region.current.name
  sap_marketing_ds7_appflow = {
    SAP_MKTCloud_INTERACTION_Full = {
      appflow_name           = "SAP_MKTCloud_INTERACTION_Full"
      appflow_description    = "SAP_MKTCloud_INTERACTION_Full"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_INTERACTIONAWS_02_CDS/YY1_InteractionAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "OnDemand"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "ID",
            "Interaction",
            "InteractionContactOrigin",
            "InteractionContactId",
            "CommunicationMedium",
            "InteractionType",
            "InteractionStatus",
            "InteractionTimeStampUTC",
            "InteractionSourceObjectType",
            "InteractionSourceObject",
            "MarketingArea",
            "CampaignID",
            "CampaignVersion",
            "MarketingLocationOrigin",
            "MarketingLocation",
            "DigitalAccount",
            "DigitalAccountType",
            "MKT_AgreementOrigin",
            "MKT_AgreementExternalID",
            "MarketingOrchestrationID",
            "CommunicationCategory",
            "InteractionWeightingFactor",
            "InteractionSentimentValue",
            "InteractionSentiment",
            "InteractionReason",
            "InteractionLanguage",
            "InteractionIsAnonymous",
            "InteractionAmount",
            "Currency",
            "InteractionLatitude",
            "InteractionLongitude",
            "SpatialReferenceSystem",
            "DeviceType",
            "InteractionDeviceName",
            "InteractionSoftwareClientName",
            "InteractionOperatingSystemName",
            "PrecedingInteractionUUID",
            "InteractionProcessingDuration",
            "InteractionPriority",
            "SourceSystemType",
            "SourceSystem",
            "InteractionSourceObjectStatus",
            "InteractionSourceObjectAddlID",
            "InteractionSourceDataURL",
            "InteractionSourceTimeStampUTC",
            "CampaignContentLinkURL",
            "CampaignContentLinkName",
            "ReferralSource",
            "ReferralSourceCategory",
            "InteractionContact",
            "RootInteraction",
            "CampaignExecutionRun",
            "SurveyResponseUUID",
            "CampaignContentLink",
            "InteractionUTCDate",
            "EmployeeInternalID",
            "EmployeeRole",
            "InteractionCreationUTCDateTime",
            "InteractionLastChangedDateTime",
            "InteractionLastChangedByUser",
            "InteractionContentSubject",
            "InteractionContent",
            "InteractionChannel",
            "YY1_TrainingVisitTime_MIA",
            "YY1_FOCUS_MIA",
            "YY1_UTM_ID_MIA",
            "YY1_TrainingComplTime_MIA",
            "YY1_DIRECTION_MIA",
            "YY1_ZYMKCOTRAV_SUBJECT_MIA",
            "YY1_FormCategory_MIA",
            "YY1_OrderType_MIA",
            "YY1_OrganisationName_MIA",
            "YY1_GAHits_MIA",
            "YY1_SALES_GROUP_MIA",
            "YY1_VoucherCampaign_MIA",
            "YY1_TrainingTitle_MIA",
            "YY1_UTM_Source_MIA",
            "YY1_UTM_Medium_MIA",
            "YY1_DIS_CHANNEL_MIA",
            "YY1_TrainingStartTime_MIA",
            "YY1_ANSW_CON_REQ_MIA",
            "YY1_Note_MIA",
            "YY1_TrainingCompStatus_MIA",
            "YY1_NPSrelevant_MIA",
            "YY1_FEEDBACK_TO_CUST_MIA",
            "YY1_UTM_Content_EN_MIA",
            "YY1_SalesRepRole_MIA",
            "YY1_SOLUTION_MIA",
            "YY1_DIVISION_MIA",
            "YY1_CARES_RELEVANT_MIA",
            "YY1_CATEGORY_MIA",
            "YY1_PARTNER2_MIA",
            "YY1_DOMINANT_MIA",
            "YY1_QualificationLevel_MIA",
            "YY1_TrainingEndTime_MIA",
            "YY1_UTM_Term_MIA",
            "YY1_REPORTED_BY_MIA",
            "YY1_GROSS_VALUE_MIA",
            "YY1_Brand_MIA",
            "YY1_TrainingID_MIA",
            "YY1_GASessionDuration_MIA",
            "YY1_TrainingScore_MIA",
            "YY1_TrainingBookingTim_MIA",
            "YY1_Description_MIA",
            "YY1_Division1_MIA",
            "YY1_SALES_ORG_MIA",
            "YY1_UTM_Campaign_MIA",
            "YY1_SALES_OFFICE_MIA",
            "YY1_GASourceMedium_MIA",
            "daysSince_LastChangeDateTime",
            "InteractionProductUUID",
            "ProductUUID",
            "ProductOrigin",
            "Product",
            "InteractionProdWeightingFactor",
            "InteractionProductSentimentVal",
            "InteractionProductAmount",
            "InteractionProductQuantity",
            "InteractionProductUnit",
            "ProductRecommendationModelType",
            "ProductRecommendationScenario",
            "InteractionProductStatus",
            "InteractionProductReason",
            "InteractionSourceItemNumber",
            "ProductName",
            "Currency_1",
            "YY1_GROSS_VALUE_PROD_MIP",
            "YY1_GEN_FEEDB_DESCR_MIP",
            "YY1_SourceitemGUID_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "ID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Interaction"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Interaction",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactId"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactId",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionTimeStampUTC"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionTimeStampUTC",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObjectType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObjectType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignVersion"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignVersion",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "MarketingLocationOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingLocationOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingLocation"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingLocation",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DigitalAccount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DigitalAccount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DigitalAccountType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DigitalAccountType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MKT_AgreementOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MKT_AgreementOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MKT_AgreementExternalID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MKT_AgreementExternalID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingOrchestrationID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingOrchestrationID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionWeightingFactor"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionWeightingFactor",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int16",
            "SOURCE_DATA_TYPE" : "Edm.Int16"
          }
        },
        {
          "sourceFields" : [
            "InteractionSentimentValue"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSentimentValue",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "InteractionSentiment"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSentiment",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionReason"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionReason",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionLanguage"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLanguage",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionIsAnonymous"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionIsAnonymous",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "InteractionAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "Currency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Currency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionLatitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLatitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "InteractionLongitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLongitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "SpatialReferenceSystem"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SpatialReferenceSystem",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DeviceType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DeviceType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionDeviceName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionDeviceName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSoftwareClientName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSoftwareClientName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionOperatingSystemName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionOperatingSystemName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PrecedingInteractionUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PrecedingInteractionUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionProcessingDuration"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProcessingDuration",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "InteractionPriority"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionPriority",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SourceSystemType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SourceSystemType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SourceSystem"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SourceSystem",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObjectStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObjectStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObjectAddlID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObjectAddlID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceDataURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceDataURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceTimeStampUTC"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceTimeStampUTC",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ReferralSource"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ReferralSource",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ReferralSourceCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ReferralSourceCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContact"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContact",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "RootInteraction"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "RootInteraction",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionRun"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionRun",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "SurveyResponseUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SurveyResponseUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLink"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLink",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionUTCDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionUTCDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "EmployeeInternalID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "EmployeeInternalID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "EmployeeRole"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "EmployeeRole",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionCreationUTCDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionCreationUTCDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionLastChangedDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLastChangedDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionLastChangedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLastChangedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContentSubject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContentSubject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionChannel"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionChannel",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingVisitTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingVisitTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_FOCUS_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_FOCUS_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_ID_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_ID_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingComplTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingComplTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_DIRECTION_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DIRECTION_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKCOTRAV_SUBJECT_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKCOTRAV_SUBJECT_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_FormCategory_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_FormCategory_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_OrderType_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_OrderType_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_OrganisationName_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_OrganisationName_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GAHits_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GAHits_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_GROUP_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_GROUP_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_VoucherCampaign_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_VoucherCampaign_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingTitle_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingTitle_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Source_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Source_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Medium_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Medium_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_DIS_CHANNEL_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DIS_CHANNEL_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingStartTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingStartTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_ANSW_CON_REQ_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ANSW_CON_REQ_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Note_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Note_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingCompStatus_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingCompStatus_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_NPSrelevant_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_NPSrelevant_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_FEEDBACK_TO_CUST_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_FEEDBACK_TO_CUST_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Content_EN_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Content_EN_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesRepRole_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesRepRole_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SOLUTION_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SOLUTION_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_DIVISION_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DIVISION_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_CARES_RELEVANT_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_CARES_RELEVANT_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_CATEGORY_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_CATEGORY_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_PARTNER2_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_PARTNER2_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_DOMINANT_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DOMINANT_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_QualificationLevel_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_QualificationLevel_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingEndTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingEndTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Term_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Term_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_REPORTED_BY_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_REPORTED_BY_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GROSS_VALUE_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GROSS_VALUE_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_Brand_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Brand_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingID_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingID_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GASessionDuration_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GASessionDuration_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingScore_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingScore_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingBookingTim_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingBookingTim_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_Description_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Description_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Division1_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Division1_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_ORG_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_ORG_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Campaign_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Campaign_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_OFFICE_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_OFFICE_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GASourceMedium_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GASourceMedium_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ProductUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ProductOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Product"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Product",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionProdWeightingFactor"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProdWeightingFactor",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int16",
            "SOURCE_DATA_TYPE" : "Edm.Int16"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductSentimentVal"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductSentimentVal",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Byte",
            "SOURCE_DATA_TYPE" : "Edm.Byte"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductQuantity"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductQuantity",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductUnit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductUnit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ProductRecommendationModelType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductRecommendationModelType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ProductRecommendationScenario"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductRecommendationScenario",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductReason"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductReason",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceItemNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceItemNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "ProductName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Currency_1"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Currency_1",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GROSS_VALUE_PROD_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GROSS_VALUE_PROD_MIP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_GEN_FEEDB_DESCR_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GEN_FEEDB_DESCR_MIP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SourceitemGUID_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SourceitemGUID_MIP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        }
      ]
    }
    SAP_MKTCloud_INTERACTION = {
      appflow_name           = "SAP_MKTCloud_INTERACTION"
      appflow_description    = "SAP_MKTCloud_INTERACTION"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_INTERACTIONAWS_02_CDS/YY1_InteractionAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "Scheduled"
        triggerProperties = {
          Scheduled = {
            scheduleExpression = "rate(1days)"
            dataPullMode       = "Incremental"
            scheduleStartTime = formatdate(
              "YYYY-MM-DD'T'04:00:00Z",
              timeadd(timestamp(), "24h")
            )
          }
        }
      }
      incremental-pull-config = {
        datetimeTypeFieldName = "InteractionUTCDate"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "ID",
            "Interaction",
            "InteractionContactOrigin",
            "InteractionContactId",
            "CommunicationMedium",
            "InteractionType",
            "InteractionStatus",
            "InteractionTimeStampUTC",
            "InteractionSourceObjectType",
            "InteractionSourceObject",
            "MarketingArea",
            "CampaignID",
            "CampaignVersion",
            "MarketingLocationOrigin",
            "MarketingLocation",
            "DigitalAccount",
            "DigitalAccountType",
            "MKT_AgreementOrigin",
            "MKT_AgreementExternalID",
            "MarketingOrchestrationID",
            "CommunicationCategory",
            "InteractionWeightingFactor",
            "InteractionSentimentValue",
            "InteractionSentiment",
            "InteractionReason",
            "InteractionLanguage",
            "InteractionIsAnonymous",
            "InteractionAmount",
            "Currency",
            "InteractionLatitude",
            "InteractionLongitude",
            "SpatialReferenceSystem",
            "DeviceType",
            "InteractionDeviceName",
            "InteractionSoftwareClientName",
            "InteractionOperatingSystemName",
            "PrecedingInteractionUUID",
            "InteractionProcessingDuration",
            "InteractionPriority",
            "SourceSystemType",
            "SourceSystem",
            "InteractionSourceObjectStatus",
            "InteractionSourceObjectAddlID",
            "InteractionSourceDataURL",
            "InteractionSourceTimeStampUTC",
            "CampaignContentLinkURL",
            "CampaignContentLinkName",
            "ReferralSource",
            "ReferralSourceCategory",
            "InteractionContact",
            "RootInteraction",
            "CampaignExecutionRun",
            "SurveyResponseUUID",
            "CampaignContentLink",
            "InteractionUTCDate",
            "EmployeeInternalID",
            "EmployeeRole",
            "InteractionCreationUTCDateTime",
            "InteractionLastChangedDateTime",
            "InteractionLastChangedByUser",
            "InteractionContentSubject",
            "InteractionContent",
            "InteractionChannel",
            "YY1_TrainingVisitTime_MIA",
            "YY1_FOCUS_MIA",
            "YY1_UTM_ID_MIA",
            "YY1_TrainingComplTime_MIA",
            "YY1_DIRECTION_MIA",
            "YY1_ZYMKCOTRAV_SUBJECT_MIA",
            "YY1_FormCategory_MIA",
            "YY1_OrderType_MIA",
            "YY1_OrganisationName_MIA",
            "YY1_GAHits_MIA",
            "YY1_SALES_GROUP_MIA",
            "YY1_VoucherCampaign_MIA",
            "YY1_TrainingTitle_MIA",
            "YY1_UTM_Source_MIA",
            "YY1_UTM_Medium_MIA",
            "YY1_DIS_CHANNEL_MIA",
            "YY1_TrainingStartTime_MIA",
            "YY1_ANSW_CON_REQ_MIA",
            "YY1_Note_MIA",
            "YY1_TrainingCompStatus_MIA",
            "YY1_NPSrelevant_MIA",
            "YY1_FEEDBACK_TO_CUST_MIA",
            "YY1_UTM_Content_EN_MIA",
            "YY1_SalesRepRole_MIA",
            "YY1_SOLUTION_MIA",
            "YY1_DIVISION_MIA",
            "YY1_CARES_RELEVANT_MIA",
            "YY1_CATEGORY_MIA",
            "YY1_PARTNER2_MIA",
            "YY1_DOMINANT_MIA",
            "YY1_QualificationLevel_MIA",
            "YY1_TrainingEndTime_MIA",
            "YY1_UTM_Term_MIA",
            "YY1_REPORTED_BY_MIA",
            "YY1_GROSS_VALUE_MIA",
            "YY1_Brand_MIA",
            "YY1_TrainingID_MIA",
            "YY1_GASessionDuration_MIA",
            "YY1_TrainingScore_MIA",
            "YY1_TrainingBookingTim_MIA",
            "YY1_Description_MIA",
            "YY1_Division1_MIA",
            "YY1_SALES_ORG_MIA",
            "YY1_UTM_Campaign_MIA",
            "YY1_SALES_OFFICE_MIA",
            "YY1_GASourceMedium_MIA",
            "daysSince_LastChangeDateTime",
            "InteractionProductUUID",
            "ProductUUID",
            "ProductOrigin",
            "Product",
            "InteractionProdWeightingFactor",
            "InteractionProductSentimentVal",
            "InteractionProductAmount",
            "InteractionProductQuantity",
            "InteractionProductUnit",
            "ProductRecommendationModelType",
            "ProductRecommendationScenario",
            "InteractionProductStatus",
            "InteractionProductReason",
            "InteractionSourceItemNumber",
            "ProductName",
            "Currency_1",
            "YY1_GROSS_VALUE_PROD_MIP",
            "YY1_GEN_FEEDB_DESCR_MIP",
            "YY1_SourceitemGUID_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "ID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Interaction"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Interaction",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactId"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactId",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionTimeStampUTC"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionTimeStampUTC",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObjectType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObjectType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignVersion"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignVersion",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "MarketingLocationOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingLocationOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingLocation"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingLocation",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DigitalAccount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DigitalAccount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DigitalAccountType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DigitalAccountType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MKT_AgreementOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MKT_AgreementOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MKT_AgreementExternalID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MKT_AgreementExternalID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingOrchestrationID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingOrchestrationID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionWeightingFactor"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionWeightingFactor",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int16",
            "SOURCE_DATA_TYPE" : "Edm.Int16"
          }
        },
        {
          "sourceFields" : [
            "InteractionSentimentValue"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSentimentValue",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "InteractionSentiment"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSentiment",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionReason"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionReason",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionLanguage"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLanguage",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionIsAnonymous"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionIsAnonymous",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "InteractionAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "Currency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Currency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionLatitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLatitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "InteractionLongitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLongitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "SpatialReferenceSystem"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SpatialReferenceSystem",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DeviceType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DeviceType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionDeviceName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionDeviceName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSoftwareClientName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSoftwareClientName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionOperatingSystemName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionOperatingSystemName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PrecedingInteractionUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PrecedingInteractionUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionProcessingDuration"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProcessingDuration",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "InteractionPriority"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionPriority",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SourceSystemType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SourceSystemType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SourceSystem"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SourceSystem",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObjectStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObjectStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceObjectAddlID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceObjectAddlID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceDataURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceDataURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceTimeStampUTC"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceTimeStampUTC",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ReferralSource"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ReferralSource",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ReferralSourceCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ReferralSourceCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContact"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContact",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "RootInteraction"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "RootInteraction",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionRun"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionRun",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "SurveyResponseUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SurveyResponseUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLink"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLink",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionUTCDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionUTCDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "EmployeeInternalID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "EmployeeInternalID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "EmployeeRole"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "EmployeeRole",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionCreationUTCDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionCreationUTCDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionLastChangedDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLastChangedDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionLastChangedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionLastChangedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContentSubject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContentSubject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionChannel"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionChannel",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingVisitTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingVisitTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_FOCUS_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_FOCUS_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_ID_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_ID_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingComplTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingComplTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_DIRECTION_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DIRECTION_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKCOTRAV_SUBJECT_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKCOTRAV_SUBJECT_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_FormCategory_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_FormCategory_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_OrderType_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_OrderType_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_OrganisationName_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_OrganisationName_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GAHits_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GAHits_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_GROUP_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_GROUP_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_VoucherCampaign_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_VoucherCampaign_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingTitle_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingTitle_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Source_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Source_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Medium_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Medium_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_DIS_CHANNEL_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DIS_CHANNEL_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingStartTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingStartTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_ANSW_CON_REQ_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ANSW_CON_REQ_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Note_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Note_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingCompStatus_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingCompStatus_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_NPSrelevant_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_NPSrelevant_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_FEEDBACK_TO_CUST_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_FEEDBACK_TO_CUST_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Content_EN_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Content_EN_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesRepRole_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesRepRole_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SOLUTION_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SOLUTION_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_DIVISION_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DIVISION_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_CARES_RELEVANT_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_CARES_RELEVANT_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_CATEGORY_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_CATEGORY_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_PARTNER2_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_PARTNER2_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_DOMINANT_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_DOMINANT_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_QualificationLevel_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_QualificationLevel_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingEndTime_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingEndTime_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Term_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Term_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_REPORTED_BY_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_REPORTED_BY_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GROSS_VALUE_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GROSS_VALUE_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_Brand_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Brand_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingID_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingID_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GASessionDuration_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GASessionDuration_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingScore_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingScore_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingBookingTim_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingBookingTim_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_Description_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Description_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Division1_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Division1_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_ORG_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_ORG_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_UTM_Campaign_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_UTM_Campaign_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_OFFICE_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_OFFICE_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GASourceMedium_MIA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GASourceMedium_MIA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ProductUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ProductOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Product"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Product",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionProdWeightingFactor"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProdWeightingFactor",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int16",
            "SOURCE_DATA_TYPE" : "Edm.Int16"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductSentimentVal"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductSentimentVal",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Byte",
            "SOURCE_DATA_TYPE" : "Edm.Byte"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductQuantity"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductQuantity",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductUnit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductUnit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ProductRecommendationModelType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductRecommendationModelType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ProductRecommendationScenario"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductRecommendationScenario",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionProductReason"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionProductReason",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionSourceItemNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionSourceItemNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "ProductName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProductName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Currency_1"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Currency_1",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_GROSS_VALUE_PROD_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GROSS_VALUE_PROD_MIP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "YY1_GEN_FEEDB_DESCR_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_GEN_FEEDB_DESCR_MIP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SourceitemGUID_MIP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SourceitemGUID_MIP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        }
      ]
    }
    SAP_MKTCloud_ASSGDCMPGNSUCCESSDATA_Full = {
      appflow_name           = "SAP_MKTCloud_ASSGDCMPGNSUCCESSDATA_Full"
      appflow_description    = "SAP_MKTCloud_ASSGDCMPGNSUCCESSDATA_Full"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_MKT_CMPGNSUCCESSAWS_02_CDS/YY1_MKT_CMPGNSUCCESSAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "OnDemand"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "ID",
            "AssgdCmpgnSuccessDataUUID",
            "Campaign",
            "ExternalCampaignID",
            "ExternalCampaignName",
            "ExternalCampaignUUID",
            "AgeRangeUpperLimit",
            "AgeRangeLowerLimit",
            "InteractionReason",
            "InteractionStatus",
            "InteractionType",
            "GenderCode",
            "CountryCode",
            "Region",
            "DeviceType",
            "AdNetwork",
            "CommunicationMedium",
            "CmpgnPerfAltvDrillDown",
            "PaidSearchKeyWordText",
            "PaidSearchSearchTermText",
            "CampaignContentLinkAliasName",
            "CampaignSuccessImportMethod",
            "CmpgnPerformanceTimeUnit",
            "SuccessDataDate",
            "InteractionUTCDate",
            "CampaignExecutionRunDate",
            "SuccessDataDateTimeZone",
            "SuccessDataLastChangeDateTime",
            "SuccessDataReplicationStatus",
            "CampaignAutomationActionUUID",
            "GenderFreeText",
            "CountryFreeText",
            "RegionFreeText",
            "DeviceFreeText",
            "AdNetworkFreeText",
            "AdServingSpendTransCurrency",
            "AdServingSpendAmount",
            "SuggestedAdServingSpendAmount",
            "OrderTransactionCurrency",
            "OrderAmount",
            "MultiTouchAttributedOrderAmt",
            "ProjectedOrderAmount",
            "OpportunityTransactionCurrency",
            "OpportunityAmount",
            "CampaignReach",
            "NumberOfImpressions",
            "NumberOfUniqueClicks",
            "NumberOfClicks",
            "NumberOfPageLikes",
            "NumberOfPostEngagements",
            "NumberOfVideoViews",
            "NumberOfWebsiteConversions",
            "NumberOfAppInstalls",
            "NumberOfAppEngagements",
            "NumberOfEventResponses",
            "NumberOfOrders",
            "NumberOfHardBounces",
            "NumberOfSoftBounces",
            "NumberOfOpenedMessages",
            "NumberOfDeliveredMessages",
            "NumberOfSentMessages",
            "NumberOfRegistrations",
            "NumberOfMktgOfferClaims",
            "NumberOfDownloads",
            "CampaignContentLinkName",
            "VideoViewedAverageInPercent",
            "CampaignContent",
            "CampaignContentName",
            "NumberOfRejectedMessages",
            "GrossRatingPoints",
            "GrossRatingPointBase",
            "NumberOfLeads",
            "NumberOfOpportunities",
            "NumberOfPhoneCalls",
            "NumberOfAppointments",
            "NumberOfFailedInteractions",
            "NumberOfMarketingOfferViews",
            "NumberOfEmailComplaints",
            "NmbrOfOpenChannelInteractions",
            "NumberOfExecutedInteractions",
            "NumberOfTasks",
            "NrOfMultiTchAttrCnvrsns",
            "ProjectedNumberOfConversions",
            "CampaignReachInPercent",
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "ID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AssgdCmpgnSuccessDataUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AssgdCmpgnSuccessDataUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "Campaign"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Campaign",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ExternalCampaignID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExternalCampaignID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ExternalCampaignName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExternalCampaignName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ExternalCampaignUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExternalCampaignUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "AgeRangeUpperLimit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AgeRangeUpperLimit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Byte",
            "SOURCE_DATA_TYPE" : "Edm.Byte"
          }
        },
        {
          "sourceFields" : [
            "AgeRangeLowerLimit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AgeRangeLowerLimit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Byte",
            "SOURCE_DATA_TYPE" : "Edm.Byte"
          }
        },
        {
          "sourceFields" : [
            "InteractionReason"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionReason",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "GenderCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GenderCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CountryCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CountryCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Region"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Region",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DeviceType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DeviceType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdNetwork"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdNetwork",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CmpgnPerfAltvDrillDown"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CmpgnPerfAltvDrillDown",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PaidSearchKeyWordText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PaidSearchKeyWordText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PaidSearchSearchTermText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PaidSearchSearchTermText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkAliasName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkAliasName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignSuccessImportMethod"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignSuccessImportMethod",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CmpgnPerformanceTimeUnit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CmpgnPerformanceTimeUnit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionUTCDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionUTCDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionRunDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionRunDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataDateTimeZone"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataDateTimeZone",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataLastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataLastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataReplicationStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataReplicationStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignAutomationActionUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignAutomationActionUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "GenderFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GenderFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CountryFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CountryFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "RegionFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "RegionFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DeviceFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DeviceFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdNetworkFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdNetworkFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdServingSpendTransCurrency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdServingSpendTransCurrency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdServingSpendAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdServingSpendAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "SuggestedAdServingSpendAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuggestedAdServingSpendAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "OrderTransactionCurrency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OrderTransactionCurrency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "OrderAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OrderAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "MultiTouchAttributedOrderAmt"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MultiTouchAttributedOrderAmt",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "ProjectedOrderAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProjectedOrderAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "OpportunityTransactionCurrency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OpportunityTransactionCurrency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "OpportunityAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OpportunityAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CampaignReach"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignReach",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfImpressions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfImpressions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfUniqueClicks"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfUniqueClicks",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfClicks"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfClicks",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfPageLikes"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfPageLikes",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfPostEngagements"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfPostEngagements",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfVideoViews"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfVideoViews",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfWebsiteConversions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfWebsiteConversions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfAppInstalls"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfAppInstalls",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfAppEngagements"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfAppEngagements",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfEventResponses"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfEventResponses",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfOrders"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfOrders",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfHardBounces"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfHardBounces",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfSoftBounces"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfSoftBounces",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfOpenedMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfOpenedMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfDeliveredMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfDeliveredMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfSentMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfSentMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfRegistrations"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfRegistrations",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfMktgOfferClaims"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfMktgOfferClaims",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfDownloads"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfDownloads",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "VideoViewedAverageInPercent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "VideoViewedAverageInPercent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CampaignContent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "NumberOfRejectedMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfRejectedMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "GrossRatingPoints"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GrossRatingPoints",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "GrossRatingPointBase"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GrossRatingPointBase",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "NumberOfLeads"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfLeads",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfOpportunities"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfOpportunities",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfPhoneCalls"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfPhoneCalls",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfAppointments"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfAppointments",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfFailedInteractions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfFailedInteractions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfMarketingOfferViews"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfMarketingOfferViews",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfEmailComplaints"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfEmailComplaints",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NmbrOfOpenChannelInteractions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NmbrOfOpenChannelInteractions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfExecutedInteractions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfExecutedInteractions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfTasks"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfTasks",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NrOfMultiTchAttrCnvrsns"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NrOfMultiTchAttrCnvrsns",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "ProjectedNumberOfConversions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProjectedNumberOfConversions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CampaignReachInPercent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignReachInPercent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        }
      ]
    }
    SAP_MKTCloud_ASSGDCMPGNSUCCESSDATA = {
      appflow_name           = "SAP_MKTCloud_ASSGDCMPGNSUCCESSDATA"
      appflow_description    = "SAP_MKTCloud_ASSGDCMPGNSUCCESSDATA"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_MKT_CMPGNSUCCESSAWS_02_CDS/YY1_MKT_CMPGNSUCCESSAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "Scheduled"
        triggerProperties = {
          Scheduled = {
            scheduleExpression = "rate(1days)"
            dataPullMode       = "Incremental"
            scheduleStartTime = formatdate(
              "YYYY-MM-DD'T'04:00:00Z",
              timeadd(timestamp(), "24h")
            )
          }
        }
      }
      incremental-pull-config = {
        datetimeTypeFieldName = "SuccessDataLastChangeDateTime"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "ID",
            "AssgdCmpgnSuccessDataUUID",
            "Campaign",
            "ExternalCampaignID",
            "ExternalCampaignName",
            "ExternalCampaignUUID",
            "AgeRangeUpperLimit",
            "AgeRangeLowerLimit",
            "InteractionReason",
            "InteractionStatus",
            "InteractionType",
            "GenderCode",
            "CountryCode",
            "Region",
            "DeviceType",
            "AdNetwork",
            "CommunicationMedium",
            "CmpgnPerfAltvDrillDown",
            "PaidSearchKeyWordText",
            "PaidSearchSearchTermText",
            "CampaignContentLinkAliasName",
            "CampaignSuccessImportMethod",
            "CmpgnPerformanceTimeUnit",
            "SuccessDataDate",
            "InteractionUTCDate",
            "CampaignExecutionRunDate",
            "SuccessDataDateTimeZone",
            "SuccessDataLastChangeDateTime",
            "SuccessDataReplicationStatus",
            "CampaignAutomationActionUUID",
            "GenderFreeText",
            "CountryFreeText",
            "RegionFreeText",
            "DeviceFreeText",
            "AdNetworkFreeText",
            "AdServingSpendTransCurrency",
            "AdServingSpendAmount",
            "SuggestedAdServingSpendAmount",
            "OrderTransactionCurrency",
            "OrderAmount",
            "MultiTouchAttributedOrderAmt",
            "ProjectedOrderAmount",
            "OpportunityTransactionCurrency",
            "OpportunityAmount",
            "CampaignReach",
            "NumberOfImpressions",
            "NumberOfUniqueClicks",
            "NumberOfClicks",
            "NumberOfPageLikes",
            "NumberOfPostEngagements",
            "NumberOfVideoViews",
            "NumberOfWebsiteConversions",
            "NumberOfAppInstalls",
            "NumberOfAppEngagements",
            "NumberOfEventResponses",
            "NumberOfOrders",
            "NumberOfHardBounces",
            "NumberOfSoftBounces",
            "NumberOfOpenedMessages",
            "NumberOfDeliveredMessages",
            "NumberOfSentMessages",
            "NumberOfRegistrations",
            "NumberOfMktgOfferClaims",
            "NumberOfDownloads",
            "CampaignContentLinkName",
            "VideoViewedAverageInPercent",
            "CampaignContent",
            "CampaignContentName",
            "NumberOfRejectedMessages",
            "GrossRatingPoints",
            "GrossRatingPointBase",
            "NumberOfLeads",
            "NumberOfOpportunities",
            "NumberOfPhoneCalls",
            "NumberOfAppointments",
            "NumberOfFailedInteractions",
            "NumberOfMarketingOfferViews",
            "NumberOfEmailComplaints",
            "NmbrOfOpenChannelInteractions",
            "NumberOfExecutedInteractions",
            "NumberOfTasks",
            "NrOfMultiTchAttrCnvrsns",
            "ProjectedNumberOfConversions",
            "CampaignReachInPercent",
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "ID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AssgdCmpgnSuccessDataUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AssgdCmpgnSuccessDataUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "Campaign"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Campaign",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ExternalCampaignID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExternalCampaignID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ExternalCampaignName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExternalCampaignName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ExternalCampaignUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExternalCampaignUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "AgeRangeUpperLimit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AgeRangeUpperLimit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Byte",
            "SOURCE_DATA_TYPE" : "Edm.Byte"
          }
        },
        {
          "sourceFields" : [
            "AgeRangeLowerLimit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AgeRangeLowerLimit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Byte",
            "SOURCE_DATA_TYPE" : "Edm.Byte"
          }
        },
        {
          "sourceFields" : [
            "InteractionReason"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionReason",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "GenderCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GenderCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CountryCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CountryCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Region"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Region",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DeviceType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DeviceType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdNetwork"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdNetwork",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CmpgnPerfAltvDrillDown"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CmpgnPerfAltvDrillDown",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PaidSearchKeyWordText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PaidSearchKeyWordText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PaidSearchSearchTermText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PaidSearchSearchTermText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkAliasName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkAliasName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignSuccessImportMethod"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignSuccessImportMethod",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CmpgnPerformanceTimeUnit"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CmpgnPerformanceTimeUnit",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "InteractionUTCDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionUTCDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionRunDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionRunDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataDateTimeZone"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataDateTimeZone",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataLastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataLastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "SuccessDataReplicationStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuccessDataReplicationStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignAutomationActionUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignAutomationActionUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "GenderFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GenderFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CountryFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CountryFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "RegionFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "RegionFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "DeviceFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "DeviceFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdNetworkFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdNetworkFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdServingSpendTransCurrency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdServingSpendTransCurrency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AdServingSpendAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AdServingSpendAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "SuggestedAdServingSpendAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SuggestedAdServingSpendAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "OrderTransactionCurrency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OrderTransactionCurrency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "OrderAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OrderAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "MultiTouchAttributedOrderAmt"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MultiTouchAttributedOrderAmt",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "ProjectedOrderAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProjectedOrderAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "OpportunityTransactionCurrency"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OpportunityTransactionCurrency",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "OpportunityAmount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "OpportunityAmount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CampaignReach"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignReach",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfImpressions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfImpressions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfUniqueClicks"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfUniqueClicks",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfClicks"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfClicks",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfPageLikes"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfPageLikes",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfPostEngagements"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfPostEngagements",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfVideoViews"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfVideoViews",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfWebsiteConversions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfWebsiteConversions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfAppInstalls"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfAppInstalls",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfAppEngagements"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfAppEngagements",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfEventResponses"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfEventResponses",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfOrders"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfOrders",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfHardBounces"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfHardBounces",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfSoftBounces"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfSoftBounces",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfOpenedMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfOpenedMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfDeliveredMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfDeliveredMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfSentMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfSentMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfRegistrations"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfRegistrations",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfMktgOfferClaims"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfMktgOfferClaims",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfDownloads"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfDownloads",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentLinkName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentLinkName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "VideoViewedAverageInPercent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "VideoViewedAverageInPercent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CampaignContent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "CampaignContentName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignContentName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "NumberOfRejectedMessages"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfRejectedMessages",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "GrossRatingPoints"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GrossRatingPoints",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "GrossRatingPointBase"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GrossRatingPointBase",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "NumberOfLeads"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfLeads",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfOpportunities"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfOpportunities",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfPhoneCalls"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfPhoneCalls",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfAppointments"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfAppointments",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfFailedInteractions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfFailedInteractions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfMarketingOfferViews"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfMarketingOfferViews",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfEmailComplaints"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfEmailComplaints",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NmbrOfOpenChannelInteractions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NmbrOfOpenChannelInteractions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfExecutedInteractions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfExecutedInteractions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NumberOfTasks"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NumberOfTasks",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int64",
            "SOURCE_DATA_TYPE" : "Edm.Int64"
          }
        },
        {
          "sourceFields" : [
            "NrOfMultiTchAttrCnvrsns"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "NrOfMultiTchAttrCnvrsns",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "ProjectedNumberOfConversions"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ProjectedNumberOfConversions",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CampaignReachInPercent"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignReachInPercent",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Decimal",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        }
      ]
    }
    SAP_MKTCloud_INTIATIVE_Full = {
      appflow_name           = "SAP_MKTCloud_INTIATIVE_Full"
      appflow_description    = "SAP_MKTCloud_INTIATIVE_Full"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_MKTINITIATIVEAWS_02_CDS/YY1_MktInitiativeAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "OnDemand"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "Campaign",
            "CampaignID",
            "CampaignName",
            "CampaignDescription",
            "CampaignCategory",
            "MarketingArea",
            "MarketingProgram",
            "MarketingProgramPhaseUUID",
            "CampaignProcessType",
            "CommunicationCategoryUUID",
            "CampaignCreatedByUser",
            "CampaignLastChgdByUser",
            "CampaignCreationDateTime",
            "CampaignLastChgdDateTime",
            "CampaignScheduleDateTime",
            "CampaignExecutionFrqcyInterval",
            "CampaignExecutionFrqcyUnitName",
            "ExportDefinition",
            "CampaignOwner",
            "CampaignLifecycleStatus",
            "CampaignStartDate",
            "CampaignEndDate",
            "MediaType",
            "CampaignPriority",
            "CampaignTimeZone",
            "MarketingPermissionIsIgnored",
            "TargetGroupUUID",
            "MarketingAgencyUUID",
            "CampaignPerfUpdateStatus",
            "YY1_MKINI_DIV_MIN_MIN",
            "YY1_SALES_REP_ROLE_MIN_MIN",
            "daysSince_LastChangeDateTime",
            "TargetGroup",
            "TargetGroupName",
            "TargetGroupDescription",
            "TargetGroupLifecycleStatus",
            "TargetGroupMemberCount",
            "ResultSetReferenceUUID",
            "ChangedOnDateTime",
            "LastChangedByUser",
            "CreationDateTime",
            "CreatedByUser",
            "TargetGroupMainResponsible",
            "TargetGroupMemberType",
            "TargetGroupMemberTypeName",
            "TargetGroupOrigin",
            "TargetGroupOriginName",
            "IsTargetGroupVersioningActive",
            "TargetGroupVersion",
            "TargetGroupLastRebuildDateTime",
            "TargetGroupCategory",
            "TargetGroupCategoryName",
            "TargetGroupIsControlGroup",
            "TargetGroupControlGroup",
            "TargetGroupControlGroupUUID",
            "MarketingArea_1",
            "MarketingAreaName",
            "SegmentationApplication",
            "SegmentationObject",
            "SegmentationObjectName",
            "TargetGroupType",
            "TargetGroupTypeName"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "Campaign"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Campaign",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignDescription"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignDescription",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingProgram"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingProgram",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "MarketingProgramPhaseUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingProgramPhaseUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignProcessType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignProcessType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategoryUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategoryUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignCreatedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignCreatedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignLastChgdByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignLastChgdByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignCreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignCreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignLastChgdDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignLastChgdDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignScheduleDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignScheduleDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionFrqcyInterval"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionFrqcyInterval",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionFrqcyUnitName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionFrqcyUnitName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ExportDefinition"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExportDefinition",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignOwner"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignOwner",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignLifecycleStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignLifecycleStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignStartDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignStartDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignEndDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignEndDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "MediaType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MediaType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignPriority"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignPriority",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignTimeZone"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignTimeZone",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingPermissionIsIgnored"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingPermissionIsIgnored",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "MarketingAgencyUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingAgencyUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignPerfUpdateStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignPerfUpdateStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_MKINI_DIV_MIN_MIN"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_MKINI_DIV_MIN_MIN",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_REP_ROLE_MIN_MIN"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_REP_ROLE_MIN_MIN",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "TargetGroup"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroup",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupDescription"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupDescription",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupLifecycleStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupLifecycleStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMemberCount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMemberCount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "ResultSetReferenceUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ResultSetReferenceUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ChangedOnDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ChangedOnDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "LastChangedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CreatedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreatedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMainResponsible"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMainResponsible",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMemberType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMemberType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMemberTypeName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMemberTypeName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupOriginName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupOriginName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "IsTargetGroupVersioningActive"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "IsTargetGroupVersioningActive",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupVersion"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupVersion",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupLastRebuildDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupLastRebuildDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupCategoryName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupCategoryName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupIsControlGroup"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupIsControlGroup",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupControlGroup"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupControlGroup",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupControlGroupUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupControlGroupUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea_1"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea_1",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingAreaName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingAreaName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SegmentationApplication"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SegmentationApplication",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SegmentationObject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SegmentationObject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SegmentationObjectName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SegmentationObjectName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupTypeName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupTypeName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        }
      ]
    }
    SAP_MKTCloud_INTIATIVE = {
      appflow_name           = "SAP_MKTCloud_INTIATIVE"
      appflow_description    = "SAP_MKTCloud_INTIATIVE"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_MKTINITIATIVEAWS_02_CDS/YY1_MktInitiativeAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "Scheduled"
        triggerProperties = {
          Scheduled = {
            scheduleExpression = "rate(1days)"
            dataPullMode       = "Incremental"
            scheduleStartTime = formatdate(
              "YYYY-MM-DD'T'04:00:00Z",
              timeadd(timestamp(), "24h")
            )
          }
        }
      }
      incremental-pull-config = {
        datetimeTypeFieldName = "ChangedOnDateTime"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "Campaign",
            "CampaignID",
            "CampaignName",
            "CampaignDescription",
            "CampaignCategory",
            "MarketingArea",
            "MarketingProgram",
            "MarketingProgramPhaseUUID",
            "CampaignProcessType",
            "CommunicationCategoryUUID",
            "CampaignCreatedByUser",
            "CampaignLastChgdByUser",
            "CampaignCreationDateTime",
            "CampaignLastChgdDateTime",
            "CampaignScheduleDateTime",
            "CampaignExecutionFrqcyInterval",
            "CampaignExecutionFrqcyUnitName",
            "ExportDefinition",
            "CampaignOwner",
            "CampaignLifecycleStatus",
            "CampaignStartDate",
            "CampaignEndDate",
            "MediaType",
            "CampaignPriority",
            "CampaignTimeZone",
            "MarketingPermissionIsIgnored",
            "TargetGroupUUID",
            "MarketingAgencyUUID",
            "CampaignPerfUpdateStatus",
            "YY1_MKINI_DIV_MIN_MIN",
            "YY1_SALES_REP_ROLE_MIN_MIN",
            "daysSince_LastChangeDateTime",
            "TargetGroup",
            "TargetGroupName",
            "TargetGroupDescription",
            "TargetGroupLifecycleStatus",
            "TargetGroupMemberCount",
            "ResultSetReferenceUUID",
            "ChangedOnDateTime",
            "LastChangedByUser",
            "CreationDateTime",
            "CreatedByUser",
            "TargetGroupMainResponsible",
            "TargetGroupMemberType",
            "TargetGroupMemberTypeName",
            "TargetGroupOrigin",
            "TargetGroupOriginName",
            "IsTargetGroupVersioningActive",
            "TargetGroupVersion",
            "TargetGroupLastRebuildDateTime",
            "TargetGroupCategory",
            "TargetGroupCategoryName",
            "TargetGroupIsControlGroup",
            "TargetGroupControlGroup",
            "TargetGroupControlGroupUUID",
            "MarketingArea_1",
            "MarketingAreaName",
            "SegmentationApplication",
            "SegmentationObject",
            "SegmentationObjectName",
            "TargetGroupType",
            "TargetGroupTypeName"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "Campaign"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Campaign",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignDescription"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignDescription",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingProgram"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingProgram",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "MarketingProgramPhaseUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingProgramPhaseUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignProcessType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignProcessType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategoryUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategoryUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignCreatedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignCreatedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignLastChgdByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignLastChgdByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignCreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignCreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignLastChgdDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignLastChgdDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignScheduleDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignScheduleDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionFrqcyInterval"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionFrqcyInterval",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignExecutionFrqcyUnitName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignExecutionFrqcyUnitName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ExportDefinition"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ExportDefinition",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignOwner"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignOwner",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignLifecycleStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignLifecycleStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignStartDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignStartDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CampaignEndDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignEndDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "MediaType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MediaType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignPriority"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignPriority",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CampaignTimeZone"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignTimeZone",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingPermissionIsIgnored"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingPermissionIsIgnored",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "MarketingAgencyUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingAgencyUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CampaignPerfUpdateStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CampaignPerfUpdateStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_MKINI_DIV_MIN_MIN"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_MKINI_DIV_MIN_MIN",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SALES_REP_ROLE_MIN_MIN"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SALES_REP_ROLE_MIN_MIN",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "TargetGroup"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroup",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupDescription"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupDescription",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupLifecycleStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupLifecycleStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMemberCount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMemberCount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "ResultSetReferenceUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ResultSetReferenceUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "ChangedOnDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ChangedOnDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "LastChangedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CreatedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreatedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMainResponsible"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMainResponsible",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMemberType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMemberType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupMemberTypeName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupMemberTypeName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupOriginName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupOriginName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "IsTargetGroupVersioningActive"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "IsTargetGroupVersioningActive",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupVersion"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupVersion",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupLastRebuildDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupLastRebuildDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupCategoryName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupCategoryName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupIsControlGroup"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupIsControlGroup",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupControlGroup"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupControlGroup",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupControlGroupUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupControlGroupUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea_1"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea_1",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingAreaName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingAreaName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SegmentationApplication"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SegmentationApplication",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SegmentationObject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SegmentationObject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "SegmentationObjectName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "SegmentationObjectName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "TargetGroupTypeName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "TargetGroupTypeName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        }
      ]
    }
    SAP_MKTCloud_EXPLICITPERMISSION_Full = {
      appflow_name           = "SAP_MKTCloud_EXPLICITPERMISSION_Full"
      appflow_description    = "SAP_MKTCloud_EXPLICITPERMISSION_Full"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_MKTPERMISSIONAWS_02_CDS/YY1_MktPermissionAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "OnDemand"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "MarketingPermissionUUID",
            "InteractionContact",
            "InteractionContactOrigin",
            "InteractionContactId",
            "CommunicationMedium",
            "CommunicationDirection",
            "ContactPermission",
            "CommunicationCategoryUUID",
            "CommunicationCategory",
            "MarketingArea",
            "PermissionUTCDateTime",
            "PermissionSourceCommMedium",
            "PermissionSourceSystemType",
            "PermissionSourceSystem",
            "PermissionSourceObjectType",
            "PermissionSourceObject",
            "PermissionNoteText",
            "CreationDateTime",
            "LastChangeDateTime",
            "daysSince_LastChangeDateTimeDA"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "MarketingPermissionUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingPermissionUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionContact"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContact",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactId"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactId",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationDirection"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationDirection",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ContactPermission"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ContactPermission",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategoryUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategoryUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionUTCDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionUTCDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceCommMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceCommMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceSystemType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceSystemType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceSystem"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceSystem",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceObjectType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceObjectType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceObject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceObject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionNoteText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionNoteText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTimeDA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTimeDA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        }
      ]
    }
    SAP_MKTCloud_EXPLICITPERMISSION = {
      appflow_name           = "SAP_MKTCloud_EXPLICITPERMISSION"
      appflow_description    = "SAP_MKTCloud_EXPLICITPERMISSION"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_MKTPERMISSIONAWS_02_CDS/YY1_MktPermissionAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "Scheduled"
        triggerProperties = {
          Scheduled = {
            scheduleExpression = "rate(1days)"
            dataPullMode       = "Incremental"
            scheduleStartTime = formatdate(
              "YYYY-MM-DD'T'04:00:00Z",
              timeadd(timestamp(), "24h")
            )
          }
        }
      }
      incremental-pull-config = {
        datetimeTypeFieldName = "LastChangeDateTime"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "MarketingPermissionUUID",
            "InteractionContact",
            "InteractionContactOrigin",
            "InteractionContactId",
            "CommunicationMedium",
            "CommunicationDirection",
            "ContactPermission",
            "CommunicationCategoryUUID",
            "CommunicationCategory",
            "MarketingArea",
            "PermissionUTCDateTime",
            "PermissionSourceCommMedium",
            "PermissionSourceSystemType",
            "PermissionSourceSystem",
            "PermissionSourceObjectType",
            "PermissionSourceObject",
            "PermissionNoteText",
            "CreationDateTime",
            "LastChangeDateTime",
            "daysSince_LastChangeDateTimeDA"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "MarketingPermissionUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingPermissionUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionContact"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContact",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactOrigin"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactOrigin",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactId"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactId",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CommunicationDirection"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationDirection",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ContactPermission"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ContactPermission",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategoryUUID"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategoryUUID",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Guid",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "CommunicationCategory"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CommunicationCategory",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MarketingArea"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MarketingArea",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionUTCDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionUTCDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceCommMedium"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceCommMedium",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceSystemType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceSystemType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceSystem"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceSystem",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceObjectType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceObjectType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionSourceObject"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionSourceObject",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PermissionNoteText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PermissionNoteText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.String",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "datetime",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTimeDA"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTimeDA",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "Edm.Int32",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        }
      ]
    }
    SAP_MKTCloud_CONTACT_Full = {
      appflow_name           = "SAP_MKTCloud_CONTACT_Full"
      appflow_description    = "SAP_MKTCloud_CONTACT_Full"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_CONTACTSAWS_02_CDS/YY1_ContactsAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "OnDemand"
      }
      s3_output_format_config = {
        fileType = "PARQUET"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "YY1_AddressTitle_MCP",
            "YY1_BUPA_NAME2_MCP",
            "YY1_SalesRole_MPS",
            "YY1_ZYMKBUPA_ATTRIB9_MCP",
            "YY1_ZYMKBUPA_ATTRIB7_MCP",
            "YY1_BUPA_ROOM_NO_ENH",
            "Longitude",
            "CreatedByUser",
            "HasMktgPermissionForDirectMail",
            "YY1_BUPA_NAME4_MCP",
            "Function",
            "FormOfAddress",
            "YY1_BUPA_PO_BOX_CIT_ENH",
            "LastChangedByUser",
            "YY1_BUPA_ACCOUNT_GROUP_MCP",
            "ValidationStatus",
            "YY1_TITLE_ENH",
            "YY1_SalesBrand_MPS",
            "AddressHouseNumber",
            "YY1_RegistrationDate_MPS",
            "IsContactPerson",
            "YY1_AcademicTitle_MPS",
            "FirstName",
            "FullName",
            "CreationDate",
            "YY1_BUPA_POSTL_COD2_ENH",
            "LanguageCode",
            "Country",
            "YY1_RegistrationSource_MPS",
            "daysSince_LastChangeDateTime",
            "YY1_ADDRSUPPL2_MPS",
            "YY1_YY1_BUPA_SPEC_KEY__MPS",
            "YY1_ActivationCode_MPS",
            "YY1_TrainingUserStatus_MPS",
            "YY1_ZYMKBUPA_ATTRIB5_MCP",
            "YY1_ZYMKBUPA_ATTRIB3_MCP",
            "PartnerFunctionName",
            "YY1_ZYMKBUPA_ATTRIB2_MCP",
            "LastChangeDateTime",
            "YY1_BUPA_FLOOR_ENH",
            "YY1_TrainingUserExtID_MPS",
            "YY1_ZYMKBUPA_ATTRIB10_MCP",
            "ImageURL",
            "ContactPersonDepartment",
            "CityName",
            "GenderCode",
            "StreetName",
            "Department",
            "YY1_EshopIDCreatedAt_MPS",
            "CorporateAccount",
            "LanguageFreeText",
            "InteractionContactType",
            "CountryFreeText",
            "FaxNumber",
            "Latitude",
            "BirthDate",
            "YY1_SalesPortfolio_MPS",
            "YY1_ZYMKBUPA_ATTRIB8_MCP",
            "YY1_ZYMKBUPA_ATTRIB6_MCP",
            "YY1_Contact_ENH",
            "YY1_ZYMKBUPA_ATTRIB1_MCP",
            "RegionFreeText",
            "LastChangeDate",
            "YY1_BUPA_ITIMITSEIT_MPS",
            "EmailAddress",
            "YY1_BUPA_BUILDING_ENH",
            "YY1_Gender_MPS",
            "YY1_BUPA_AUTH_GROUP_ENH",
            "YY1_BUPA_POBOX_CTRY_ENH",
            "ContactPostalCode",
            "MaritalStatus",
            "MobileNumber",
            "YY1_TrainingUserName_MPS",
            "PhoneNumber",
            "ChangedOnDateTime",
            "YY1_ORGNAMESUP_MPS",
            "YY1_IS_EMPL_MPS",
            "LastName",
            "AddressRegion",
            "YY1_ZYMKBUPA_ATTRIB4_MCP",
            "YY1_Title2_MPS",
            "LastChangedDate",
            "YY1_BUPA_PO_BOX_1_ENH",
            "YY1_ZYMKBUPA_CUSTOMER__MCP",
            "YY1_Username_MPS",
            "YY1_BUPA_LETTERSALU_ENH",
            "YY1_ZYMKBUPA_CLASSIFIC_MCP",
            "IsConsumer",
            "InteractionContact",
            "YY1_BUPA_NOT_RELEASED_ENH",
            "YY1_BUPA_NAME3_MCP",
            "YY1_Implant_Volume_MPS",
            "CompanyName",
            "WebsiteURL",
            "CreationDateTime",
            "YY1_BUPA_ITMITGLIE_MPS",
            "InteractnCntctConsumerAccount",
            "YY1_NICKNAME_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "YY1_AddressTitle_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_AddressTitle_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NAME2_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NAME2_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesRole_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesRole_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB9_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB9_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB7_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB7_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ROOM_NO_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ROOM_NO_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Longitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Longitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "double",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CreatedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreatedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "HasMktgPermissionForDirectMail"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "HasMktgPermissionForDirectMail",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NAME4_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NAME4_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Function"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Function",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FormOfAddress"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FormOfAddress",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_PO_BOX_CIT_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_PO_BOX_CIT_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ACCOUNT_GROUP_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ACCOUNT_GROUP_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ValidationStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ValidationStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TITLE_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TITLE_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesBrand_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesBrand_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AddressHouseNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AddressHouseNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_RegistrationDate_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_RegistrationDate_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "IsContactPerson"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "IsContactPerson",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_AcademicTitle_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_AcademicTitle_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FirstName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FirstName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FullName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FullName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_POSTL_COD2_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_POSTL_COD2_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LanguageCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LanguageCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Country"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Country",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_RegistrationSource_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_RegistrationSource_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "YY1_ADDRSUPPL2_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ADDRSUPPL2_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_YY1_BUPA_SPEC_KEY__MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_YY1_BUPA_SPEC_KEY__MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ActivationCode_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ActivationCode_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingUserStatus_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingUserStatus_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB5_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB5_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB3_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB3_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PartnerFunctionName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PartnerFunctionName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB2_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB2_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_FLOOR_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_FLOOR_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingUserExtID_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingUserExtID_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB10_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB10_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ImageURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ImageURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ContactPersonDepartment"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ContactPersonDepartment",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CityName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CityName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "GenderCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GenderCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "StreetName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "StreetName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Department"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Department",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_EshopIDCreatedAt_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_EshopIDCreatedAt_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CorporateAccount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CorporateAccount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LanguageFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LanguageFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CountryFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CountryFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FaxNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FaxNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Latitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Latitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "double",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "BirthDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "BirthDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesPortfolio_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesPortfolio_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB8_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB8_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB6_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB6_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Contact_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Contact_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB1_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB1_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "RegionFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "RegionFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangeDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangeDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ITIMITSEIT_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ITIMITSEIT_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "EmailAddress"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "EmailAddress",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_BUILDING_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_BUILDING_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Gender_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Gender_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_AUTH_GROUP_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_AUTH_GROUP_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_POBOX_CTRY_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_POBOX_CTRY_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ContactPostalCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ContactPostalCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MaritalStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MaritalStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MobileNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MobileNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingUserName_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingUserName_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PhoneNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PhoneNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ChangedOnDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ChangedOnDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_ORGNAMESUP_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ORGNAMESUP_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_IS_EMPL_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_IS_EMPL_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "LastName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AddressRegion"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AddressRegion",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB4_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB4_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Title2_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Title2_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangedDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangedDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_PO_BOX_1_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_PO_BOX_1_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_CUSTOMER__MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_CUSTOMER__MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Username_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Username_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_LETTERSALU_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_LETTERSALU_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_CLASSIFIC_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_CLASSIFIC_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "IsConsumer"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "IsConsumer",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "InteractionContact"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContact",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NOT_RELEASED_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NOT_RELEASED_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NAME3_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NAME3_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Implant_Volume_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Implant_Volume_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CompanyName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CompanyName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "WebsiteURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "WebsiteURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ITMITGLIE_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ITMITGLIE_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractnCntctConsumerAccount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractnCntctConsumerAccount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_NICKNAME_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_NICKNAME_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        }
      ]
    }
    SAP_MKTCloud_CONTACT = {
      appflow_name           = "SAP_MKTCloud_CONTACT"
      appflow_description    = "SAP_MKTCloud_CONTACT"
      dest_conn_type         = "S3"
      dest_bucket_name       = "stg-dlk-${var.env}-ds-7-raw"
      src_conn_type          = "SAPOData"
      src_conn_obj_path      = "/sap/opu/odata/sap/YY1_CONTACTSAWS_02_CDS/YY1_ContactsAWS_02"
      connector_profile_name = "stg-dlk-sap-odata-marketing-connection"
      trigger-config = {
        triggerType = "Scheduled"
        triggerProperties = {
          Scheduled = {
            scheduleExpression = "rate(1days)"
            dataPullMode       = "Incremental"
            scheduleStartTime = formatdate(
              "YYYY-MM-DD'T'04:00:00Z",
              timeadd(timestamp(), "24h")
            )
          }
        }
      }
      incremental-pull-config = {
        datetimeTypeFieldName = "LastChangeDateTime"
      }
      flow_tasks = [
        {
          "sourceFields" : [
            "YY1_AddressTitle_MCP",
            "YY1_BUPA_NAME2_MCP",
            "YY1_SalesRole_MPS",
            "YY1_ZYMKBUPA_ATTRIB9_MCP",
            "YY1_ZYMKBUPA_ATTRIB7_MCP",
            "YY1_BUPA_ROOM_NO_ENH",
            "Longitude",
            "CreatedByUser",
            "HasMktgPermissionForDirectMail",
            "YY1_BUPA_NAME4_MCP",
            "Function",
            "FormOfAddress",
            "YY1_BUPA_PO_BOX_CIT_ENH",
            "LastChangedByUser",
            "YY1_BUPA_ACCOUNT_GROUP_MCP",
            "ValidationStatus",
            "YY1_TITLE_ENH",
            "YY1_SalesBrand_MPS",
            "AddressHouseNumber",
            "YY1_RegistrationDate_MPS",
            "IsContactPerson",
            "YY1_AcademicTitle_MPS",
            "FirstName",
            "FullName",
            "CreationDate",
            "YY1_BUPA_POSTL_COD2_ENH",
            "LanguageCode",
            "Country",
            "YY1_RegistrationSource_MPS",
            "daysSince_LastChangeDateTime",
            "YY1_ADDRSUPPL2_MPS",
            "YY1_YY1_BUPA_SPEC_KEY__MPS",
            "YY1_ActivationCode_MPS",
            "YY1_TrainingUserStatus_MPS",
            "YY1_ZYMKBUPA_ATTRIB5_MCP",
            "YY1_ZYMKBUPA_ATTRIB3_MCP",
            "PartnerFunctionName",
            "YY1_ZYMKBUPA_ATTRIB2_MCP",
            "LastChangeDateTime",
            "YY1_BUPA_FLOOR_ENH",
            "YY1_TrainingUserExtID_MPS",
            "YY1_ZYMKBUPA_ATTRIB10_MCP",
            "ImageURL",
            "ContactPersonDepartment",
            "CityName",
            "GenderCode",
            "StreetName",
            "Department",
            "YY1_EshopIDCreatedAt_MPS",
            "CorporateAccount",
            "LanguageFreeText",
            "InteractionContactType",
            "CountryFreeText",
            "FaxNumber",
            "Latitude",
            "BirthDate",
            "YY1_SalesPortfolio_MPS",
            "YY1_ZYMKBUPA_ATTRIB8_MCP",
            "YY1_ZYMKBUPA_ATTRIB6_MCP",
            "YY1_Contact_ENH",
            "YY1_ZYMKBUPA_ATTRIB1_MCP",
            "RegionFreeText",
            "LastChangeDate",
            "YY1_BUPA_ITIMITSEIT_MPS",
            "EmailAddress",
            "YY1_BUPA_BUILDING_ENH",
            "YY1_Gender_MPS",
            "YY1_BUPA_AUTH_GROUP_ENH",
            "YY1_BUPA_POBOX_CTRY_ENH",
            "ContactPostalCode",
            "MaritalStatus",
            "MobileNumber",
            "YY1_TrainingUserName_MPS",
            "PhoneNumber",
            "ChangedOnDateTime",
            "YY1_ORGNAMESUP_MPS",
            "YY1_IS_EMPL_MPS",
            "LastName",
            "AddressRegion",
            "YY1_ZYMKBUPA_ATTRIB4_MCP",
            "YY1_Title2_MPS",
            "LastChangedDate",
            "YY1_BUPA_PO_BOX_1_ENH",
            "YY1_ZYMKBUPA_CUSTOMER__MCP",
            "YY1_Username_MPS",
            "YY1_BUPA_LETTERSALU_ENH",
            "YY1_ZYMKBUPA_CLASSIFIC_MCP",
            "IsConsumer",
            "InteractionContact",
            "YY1_BUPA_NOT_RELEASED_ENH",
            "YY1_BUPA_NAME3_MCP",
            "YY1_Implant_Volume_MPS",
            "CompanyName",
            "WebsiteURL",
            "CreationDateTime",
            "YY1_BUPA_ITMITGLIE_MPS",
            "InteractnCntctConsumerAccount",
            "YY1_NICKNAME_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "PROJECTION"
          },
          "taskType" : "Filter",
          "taskProperties" : {}
        },
        {
          "sourceFields" : [
            "YY1_AddressTitle_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_AddressTitle_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NAME2_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NAME2_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesRole_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesRole_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB9_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB9_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB7_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB7_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ROOM_NO_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ROOM_NO_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Longitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Longitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "double",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "CreatedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreatedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "HasMktgPermissionForDirectMail"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "HasMktgPermissionForDirectMail",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NAME4_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NAME4_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Function"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Function",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FormOfAddress"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FormOfAddress",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_PO_BOX_CIT_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_PO_BOX_CIT_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangedByUser"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangedByUser",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ACCOUNT_GROUP_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ACCOUNT_GROUP_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ValidationStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ValidationStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TITLE_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TITLE_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesBrand_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesBrand_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AddressHouseNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AddressHouseNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_RegistrationDate_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_RegistrationDate_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "IsContactPerson"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "IsContactPerson",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_AcademicTitle_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_AcademicTitle_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FirstName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FirstName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FullName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FullName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_POSTL_COD2_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_POSTL_COD2_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LanguageCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LanguageCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Country"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Country",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_RegistrationSource_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_RegistrationSource_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "daysSince_LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "daysSince_LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "integer",
            "SOURCE_DATA_TYPE" : "Edm.Int32"
          }
        },
        {
          "sourceFields" : [
            "YY1_ADDRSUPPL2_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ADDRSUPPL2_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_YY1_BUPA_SPEC_KEY__MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_YY1_BUPA_SPEC_KEY__MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ActivationCode_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ActivationCode_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingUserStatus_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingUserStatus_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB5_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB5_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB3_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB3_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PartnerFunctionName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PartnerFunctionName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB2_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB2_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangeDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangeDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_FLOOR_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_FLOOR_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingUserExtID_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingUserExtID_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB10_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB10_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ImageURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ImageURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ContactPersonDepartment"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ContactPersonDepartment",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CityName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CityName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "GenderCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "GenderCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "StreetName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "StreetName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Department"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Department",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_EshopIDCreatedAt_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_EshopIDCreatedAt_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "CorporateAccount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CorporateAccount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LanguageFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LanguageFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractionContactType"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContactType",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CountryFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CountryFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "FaxNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "FaxNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "Latitude"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "Latitude",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "double",
            "SOURCE_DATA_TYPE" : "Edm.Decimal"
          }
        },
        {
          "sourceFields" : [
            "BirthDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "BirthDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_SalesPortfolio_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_SalesPortfolio_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB8_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB8_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB6_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB6_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Contact_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Contact_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB1_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB1_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "RegionFreeText"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "RegionFreeText",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangeDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangeDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ITIMITSEIT_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ITIMITSEIT_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "EmailAddress"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "EmailAddress",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_BUILDING_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_BUILDING_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Gender_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Gender_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_AUTH_GROUP_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_AUTH_GROUP_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_POBOX_CTRY_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_POBOX_CTRY_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ContactPostalCode"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ContactPostalCode",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MaritalStatus"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MaritalStatus",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "MobileNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "MobileNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_TrainingUserName_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_TrainingUserName_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "PhoneNumber"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "PhoneNumber",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "ChangedOnDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "ChangedOnDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_ORGNAMESUP_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ORGNAMESUP_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_IS_EMPL_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_IS_EMPL_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "LastName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "AddressRegion"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "AddressRegion",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_ATTRIB4_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_ATTRIB4_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Title2_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Title2_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "LastChangedDate"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "LastChangedDate",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_PO_BOX_1_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_PO_BOX_1_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_CUSTOMER__MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_CUSTOMER__MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Username_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Username_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_LETTERSALU_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_LETTERSALU_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_ZYMKBUPA_CLASSIFIC_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_ZYMKBUPA_CLASSIFIC_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "IsConsumer"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "IsConsumer",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "InteractionContact"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractionContact",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.Guid"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NOT_RELEASED_ENH"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NOT_RELEASED_ENH",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "boolean",
            "SOURCE_DATA_TYPE" : "Edm.Boolean"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_NAME3_MCP"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_NAME3_MCP",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_Implant_Volume_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_Implant_Volume_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CompanyName"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CompanyName",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "WebsiteURL"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "WebsiteURL",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "CreationDateTime"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "CreationDateTime",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "timestamp",
            "SOURCE_DATA_TYPE" : "datetime"
          }
        },
        {
          "sourceFields" : [
            "YY1_BUPA_ITMITGLIE_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_BUPA_ITMITGLIE_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "InteractnCntctConsumerAccount"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "InteractnCntctConsumerAccount",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        },
        {
          "sourceFields" : [
            "YY1_NICKNAME_MPS"
          ],
          "connectorOperator" : {
            "SAPOData" : "NO_OP"
          },
          "destinationField" : "YY1_NICKNAME_MPS",
          "taskType" : "Map",
          "taskProperties" : {
            "DESTINATION_DATA_TYPE" : "string",
            "SOURCE_DATA_TYPE" : "Edm.String"
          }
        }
      ]
    }
  }
  common_tags = {
    Project   = "stg-dlk"
    ManagedBy = "Terraform"
  }
  project_code         = ["stg-dlk-${var.env}"]
  data_source_name     = ["ds1", "ds2", "ds3", "ds4", "ds5", "ds6", "ds7", "ds10", "ds11", "ds12", "ds13", "ds100"]
  bucket_type          = ["raw", "refined"]
  db_names             = [for values in setproduct(local.project_code, local.data_source_name, local.bucket_type, ["db"]) : join("-", values)]
  lf_tags = {
    business_unit_prh1 = [
      "1_surgical",
      "2_prosthetics",
      "3_regen",
      "4_4",
      "5_cadcam",
      "99_others"
    ]
    data_contents_patient = [
      "true",
      "false"
    ]
    data_contents_production = [
      "true",
      "false"
    ]
    data_contents_personal = [
      "true",
      "false"
    ]
    data_confidentialitylevel = [
      "public",
      "internal",
      "personal",
      "confidential",
      "strictly_confidential"
    ]
    data_zone = [
      "raw",
      "refined",
      "curated"
    ]
    sales = [
      "true",
      "false"
    ]
    complaints  = [
      "true",
      "false"
    ]
  }

#   # ext_bucket_name         = "stg-dlk-sbx-ds-${var.datasource_number}-ext"
#   raw_bucket_name           = "stg-dlk-sbx-ds-${var.datasource_number}-raw"
#   refined_bucket_name       = "stg-dlk-sbx-ds-${var.datasource_number}-refined"
#   datasource_bucket_folder  = "events_feed/events_jsonl_gzip/"
#   artifacts_bucket_name     = "stg-dlk-sbx-code-artifacts"
#   raw_database_name         = "stg-dlk-sbx-ds${var.datasource_number}-raw-db"
#   raw_role_name             = "stg-dlk-sbx-ds${var.datasource_number}-source-to-raw-glue-job-role"
#   raw_script_name           = "stg-dlk-sbx-ds${var.datasource_number}-job-source-to-raw"
#   refined_database_name     = "stg-dlk-sbx-ds${var.datasource_number}-refined-db"
#   refined_role_name         = "stg-dlk-sbx-ds${var.datasource_number}-raw-to-refined-glue-job-role"
#   refined_script_name       = "stg-dlk-sbx-ds${var.datasource_number}-job-raw-to-refined"
#   kms_key_arn               = "arn:aws:kms:eu-west-1:816247855850:key/396cd8ff-4b3d-4b17-9df4-9449185fdd2e"
#   ext_user_name             = "ds${var.datasource_number}_sap_cdp_ext_user"
#   # ext_role_name           = "ds${var.datasource_number}_sap_cdp_ext_role"
#   sapcdc_api_secret_name   = "stg/dlk/sapcdc/ds7/secrets"
}

############
## COMMON ##
############ 

### Create DS7 Glue Database Raw
module "ds7_stg_dlk_glue_db_raw" {
  source = "./modules/glue"

  # KMS key for the catalog encryption settings
  kms_key_arn = var.external_kms_key_arn

  create_glue_catalog_db      = true
  create_glue_crawler         = false
  create_glue_connection      = false
  glue_catalog_db_name        = local.db_names[12]
  glue_catalog_db_description = "Glue catalog db for ds7 raw zone."
  glue_location_uri           = "s3://stg-dlk-${var.env}-ds-7-raw"

  ### TAGS
  tags = local.common_tags
}

### Add LF-Tags to Databases

resource "aws_lakeformation_lf_tag" "tags" {
  for_each = local.lf_tags

  key    = each.key
  values = each.value
}

resource "aws_lakeformation_resource_lf_tags" "ds7_tf_tags_database_raw" {

  database {
    name = module.ds7_stg_dlk_glue_db_raw.glue_catalog_db_name
  }

  lf_tag {
    key   = "data_contents_patient"
    value = "false"
  }

  lf_tag {
    key   = "data_contents_production"
    value = "false"
  }

  lf_tag {
    key   = "data_contents_personal"
    value = "true"
  }

  lf_tag {
    key   = "data_confidentialitylevel"
    value = "strictly_confidential"
  }

  lf_tag {
    key   = "data_zone"
    value = "raw"
  }

  lf_tag {
    key   = "sales"
    value = "false"
  }

  lf_tag {
    key   = "complaints"
    value = "false"
  }

  depends_on = [aws_lakeformation_lf_tag.tags, module.ds7_stg_dlk_glue_db_raw.glue_catalog_db_name]

}

### AppFlow

### AppFlow Glue Catalog Role Template
resource "aws_iam_role" "ds7_appflow_glue_catalog_role" {
  name = "stg-dlk-${var.env}-ds-7-appflow-glue-catalog-role"

  assume_role_policy = templatefile("${path.module}/templates/arn_like_assume_role_policy.tpl", {
    service    = "appflow.amazonaws.com"
    account_id = local.account_id
  })

  inline_policy {

    name = "stg-dlk-${var.env}-ds-7-appflow-glue-catalog-policy"
    policy = templatefile("${path.module}/templates/appflow_glue_catalog_policy.json", {
      region      = local.region
      account_id  = local.account_id
      kms_key_arn = var.external_kms_key_arn
      glue_db     = "arn:aws:glue:${local.region}:${local.account_id}:database/${module.ds7_stg_dlk_glue_db_raw.glue_catalog_db_name}"
      glue_table  = "arn:aws:glue:${local.region}:${local.account_id}:table/${module.ds7_stg_dlk_glue_db_raw.glue_catalog_db_name}/*"
    })
  }

  tags = local.common_tags
}

data "aws_secretsmanager_secret_version" "current_sap_marketing_cloud" {
  secret_id = "stg/dlk/appflow/sap-marketing-cloud"
}

data "aws_secretsmanager_secret_version" "current_sap_marketing_cloud_prod" {
  count     = var.env == "prod" ? 1 : 0
  secret_id = "stg/dlk/prod/appflow/sap-marketing-cloud"
}

module "appflow_sap_marketing_cloud_sbx" {
  count           = var.env != "prod" ? 1 : 0
  source          = "./modules/appflow"
  name            = "stg-dlk-sap-odata-marketing-connection"
  connector_type  = "SAPOData"
  connection_mode = "Public"
  kms_arn         = var.external_kms_key_arn
  connector_profile_credentials = {
    password = jsondecode(data.aws_secretsmanager_secret_version.current_sap_marketing_cloud.secret_string)["password"]
    username = jsondecode(data.aws_secretsmanager_secret_version.current_sap_marketing_cloud.secret_string)["username"]
  }
  connector_profile_properties = {
    application_host_url     = "https://my303161-api.s4hana.ondemand.com"
    application_service_path = "/sap/opu/odata/iwfnd/catalogservice;v=2"
    client_number            = 200
    logon_language           = "EN"
    port_number              = 443
  }
  create_appflow            = true
  appflow_map               = local.sap_marketing_ds7_appflow
  tags                      = local.common_tags
  dest_bucket_name          = "stg-dlk-${var.env}-ds-7-raw"
  cross_account_role        = var.cross_account_role
  appflow_glue_role_arn     = aws_iam_role.ds7_appflow_glue_catalog_role.arn
  appflow_glue_db_name      = module.ds7_stg_dlk_glue_db_raw.glue_catalog_db_name
  appflow_glue_table_prefix = "ds7"
}
