
resource "aws_appflow_connector_profile" "this" {
  name            = var.name
  connector_type  = var.connector_type
  connection_mode = var.connection_mode
  kms_arn         = var.kms_arn

  connector_profile_config {

    connector_profile_credentials {
      sapo_data {
        basic_auth_credentials {
          password = var.connector_profile_credentials["password"]
          username = var.connector_profile_credentials["username"]
        }
      }
    }

    connector_profile_properties {
      sapo_data {
        application_host_url     = var.connector_profile_properties["application_host_url"]
        application_service_path = var.connector_profile_properties["application_service_path"]
        client_number            = var.connector_profile_properties["client_number"]
        #logon_language = var.connector_profile_properties["logon_language"]
        port_number               = var.connector_profile_properties["port_number"]
        private_link_service_name = try(var.connector_profile_properties["private_link_service_name"], null)
      }
    }
  }
}

resource "aws_appflow_flow" "this" {
  depends_on = [aws_appflow_connector_profile.this]
  for_each   = var.create_appflow ? var.appflow_map : {}

  name        = each.value.appflow_name
  description = each.value.appflow_description
  kms_arn     = var.kms_arn
  lifecycle {
    ignore_changes = [
      task
    ]
  }
  destination_flow_config {
    connector_type = each.value.dest_conn_type
    destination_connector_properties {
      s3 {
        bucket_name = each.value.dest_bucket_name
        s3_output_format_config {
          file_type = try(each.value.s3_output_format_config.fileType, "JSON")
          prefix_config {
            prefix_format = "HOUR"
            prefix_type   = "PATH"
          }
          aggregation_config {
            aggregation_type = "None"
          }
        }
      }
    }
  }
  source_flow_config {
    connector_type = each.value.src_conn_type
    source_connector_properties {
      sapo_data {
        object_path = each.value.src_conn_obj_path
      }
    }
    connector_profile_name = each.value.connector_profile_name
    dynamic "incremental_pull_config" {
      for_each = each.value.incremental-pull-config == null ? {} : each.value.incremental-pull-config
      content {
        datetime_type_field_name = try(each.value.incremental-pull-config.datetimeTypeFieldName, null)
      }
    }
  }
  dynamic "task" {
    for_each = each.value.flow_tasks
    content {
      source_fields = task.value.sourceFields
      task_type     = task.value.taskType
      connector_operator {
        sapo_data = task.value.connectorOperator.SAPOData
      }
      destination_field = task.value.destinationField
      task_properties = {
        DESTINATION_DATA_TYPE = try(task.value.taskProperties.DESTINATION_DATA_TYPE, null)
        SOURCE_DATA_TYPE      = try(task.value.taskProperties.SOURCE_DATA_TYPE, null)
        DATA_TYPE             = try(task.value.taskProperties.DATA_TYPE, null)
        VALUE                 = try(task.value.taskProperties.VALUE, null)
      }
    }
  }
  trigger_config {
    trigger_type = each.value.trigger-config.triggerType
    dynamic "trigger_properties" {
      for_each = each.value.trigger-config.triggerProperties == null ? {} : each.value.trigger-config.triggerProperties
      content {
        scheduled {
          schedule_expression = try(each.value.trigger-config.triggerProperties.Scheduled.scheduleExpression, null)
          data_pull_mode      = try(each.value.trigger-config.triggerProperties.Scheduled.dataPullMode, null)
          schedule_start_time = try(each.value.trigger-config.triggerProperties.Scheduled.scheduleStartTime, null)
        }
      }
    }
  }
  tags = var.tags
}

resource "null_resource" "update_appflows" {
  depends_on = [aws_appflow_flow.this]
  for_each   = var.create_appflow ? var.appflow_map : {}
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]
    command     = <<EOF
      set -e
      CREDENTIALS=(`aws sts assume-role \
        --role-arn ${var.cross_account_role} \
        --role-session-name "db-migration-cli" \
        --query "[Credentials.AccessKeyId,Credentials.SecretAccessKey,Credentials.SessionToken]" \
        --output text`)

      unset AWS_PROFILE
      export AWS_DEFAULT_REGION=eu-west-1
      export AWS_ACCESS_KEY_ID="$${CREDENTIALS[0]}"
      export AWS_SECRET_ACCESS_KEY="$${CREDENTIALS[1]}"
      export AWS_SESSION_TOKEN="$${CREDENTIALS[2]}"

      sapodata="${each.value.sapodata_aditional_params == null ? "{\\\"objectPath\\\":\\\"${each.value.src_conn_obj_path}\\\"}" : "{\\\"objectPath\\\":\\\"${each.value.src_conn_obj_path}\\\", \\\"parallelismConfig\\\": { \\\"maxParallelism\\\": ${each.value.sapodata_aditional_params.parallelismConfig.maxParallelism} }, \\\"paginationConfig\\\": { \\\"maxPageSize\\\": ${each.value.sapodata_aditional_params.paginationConfig.maxPageSize} }}"}"
      source_flow_config="\"connectorType\":\"SAPOData\",\"connectorProfileName\":\"${var.name}\",\"sourceConnectorProperties\":{\"SAPOData\":"$sapodata"}"

      incremental_pull_config="${each.value.incremental-pull-config == null ? "" : ", \\\"incrementalPullConfig\\\":{\\\"datetimeTypeFieldName\\\":\\\"${each.value.incremental-pull-config.datetimeTypeFieldName}\\\"}"}"
      source_flow_config+=$incremental_pull_config

      

      aws appflow update-flow --flow-name '${each.value.appflow_name}' \
                  --source-flow-config  "{$source_flow_config}" \
                  --destination-flow-config-list '${var.name == "stg-dlk-sap-odata-marketing-connection" ? local.marketing_dest_config : local.dest_config}' \
                  --tasks '${replace("${jsonencode([for l in each.value.flow_tasks : { for k, v in l : k => v if v != null }])}", "/(\"[\\w]*\":null,)|(,?\"[\\w]*\":null)/", "")}' \
                  --trigger-config  '${jsonencode({ for k, v in each.value.trigger-config : k => v if v != null })}' \
                  --description '${each.value.appflow_description}' \
                  --metadata-catalog-config 'glueDataCatalog={roleArn='${var.appflow_glue_role_arn}',databaseName='${var.appflow_glue_db_name}',tablePrefix='${var.appflow_glue_table_prefix}'}'
    EOF
  }
  triggers = {
    # run the update_appflow if any of the parameters are changed
    glue_role_arn                          = var.appflow_glue_role_arn,
    glue_db_name                           = var.appflow_glue_db_name,
    table_prefix                           = var.appflow_glue_table_prefix,
    trigger_config                         = each.value.trigger-config.triggerType,
    trigger_schedule                       = try(each.value.trigger-config.triggerProperties.Scheduled.scheduleExpression, null),
    trigger_schedule_start_time            = try(each.value.trigger-config.triggerProperties.Scheduled.scheduleStartTime, null),
    appflow_description                    = each.value.appflow_description,
    sapodata_aditional_params_maxParallism = try(each.value.sapodata_aditional_params.parallelismConfig.maxParallelism, null),
    sapodata_aditional_params_maxPageSize  = try(each.value.sapodata_aditional_params.paginationConfig.maxPageSize, null)
  }
}
