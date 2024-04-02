data "aws_partition" "current" {}
data "aws_region" "current" {}
data "aws_caller_identity" "current" {}



# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/glue_catalog_database
# Creates the database 
resource "aws_glue_catalog_database" "this" {
  count = var.create_glue_catalog_db ? 1 : 0

  name         = var.glue_catalog_db_name
  description  = try(var.glue_catalog_db_description, null)
  location_uri = try(var.glue_location_uri, null)
  parameters   = try(var.glue_db_parameters, null)

  dynamic "create_table_default_permission" {
    for_each = var.create_table_default_permission != null ? [true] : []
    content {
      permissions = try(var.create_table_default_permission.permissions, null)

      dynamic "principal" {
        for_each = try(var.create_table_default_permission.principal, null) != null ? [true] : []
        content {
          data_lake_principal_identifier = try(var.create_table_default_permission.principal.data_lake_principal_identifier, null)
        }
      }
    }
  }
}

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/glue_crawler
resource "aws_glue_crawler" "this" {
  count = var.create_glue_crawler ? 1 : 0

  name                   = var.glue_crawler_name
  description            = try(var.glue_crawler_description, null)
  database_name          = var.glue_catalog_db_name
  role                   = try(var.glue_crawler_role, null)
  schedule               = try(var.glue_crawler_schedule, null)
  classifiers            = try(var.glue_crawler_classifiers, null)
  configuration          = try(var.glue_crawler_configuration, null)
  security_configuration = try(var.glue_security_configuration, null)
  table_prefix           = try(var.glue_table_prefix, null)
  tags                   = var.tags

  dynamic "s3_target" {
    for_each = var.s3_target != null ? var.s3_target : []
    content {
      path                = s3_target.value.path
      connection_name     = try(s3_target.value.connection_name, null)
      exclusions          = try(s3_target.value.exclusions, null)
      sample_size         = try(s3_target.value.sample_size, null)
      event_queue_arn     = try(s3_target.value.event_queue_arn, null)
      dlq_event_queue_arn = try(s3_target.value.dlq_event_queue_arn, null)
    }
  }

  dynamic "catalog_target" {
    for_each = var.glue_catalog_target != null ? var.glue_catalog_target : []
    content {
      database_name = glue_catalog_target.value.glue_catalog_db_name
      tables        = glue_catalog_target.value.tables
    }
  }

  dynamic "schema_change_policy" {
    for_each = var.schema_change_policy != null ? [true] : []
    content {
      delete_behavior = var.schema_change_policy.delete_behavior
      update_behavior = var.schema_change_policy.update_behavior
    }
  }

  dynamic "recrawl_policy" {
    for_each = var.recrawl_policy != null ? [true] : []
    content {
      recrawl_behavior = var.recrawl_policy.recrawl_behavior
    }
  }

  dynamic "lake_formation_configuration" {
    for_each = var.glue_lake_formation_configuration != null ? [true] : []
    content {
      account_id                     = var.glue_lake_formation_configuration.account_id
      use_lake_formation_credentials = var.glue_lake_formation_configuration.use_lake_formation_credentials
    }
  }
}

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/glue_job
resource "aws_glue_job" "this" {
  count = var.create_glue_job ? 1 : 0

  name                      = var.glue_job_name
  role_arn                  = var.glue_job_role_arn
  description               = try(var.glue_job_description, null)
  connections               = var.create_glue_connection ? [aws_glue_connection.this[0].name] : var.glue_job_connections != null ? var.glue_job_connections : null
  default_arguments         = try(var.glue_job_default_arguments, null)
  non_overridable_arguments = try(var.glue_job_non_overridable_arguments, null)
  glue_version              = try(var.glue_version, null)
  timeout                   = try(var.glue_job_timeout, null)
  number_of_workers         = try(var.glue_job_number_of_workers, null)
  worker_type               = try(var.glue_job_worker_type, null)
  max_capacity              = try(var.glue_job_max_capacity, null)
  security_configuration    = try(var.glue_job_security_configuration, null)
  max_retries               = try(var.glue_job_max_retries, null)

  dynamic "command" {
    for_each = var.glue_job_command != null ? [true] : []
    content {
      name            = try(var.glue_job_command.name, null)
      script_location = try(var.glue_job_command.script_location, null)
      python_version  = try(var.glue_job_command.python_version, null)
    }
  }

  dynamic "notification_property" {
    for_each = var.glue_job_notification_property != null ? [true] : []
    content {
      notify_delay_after = var.glue_job_notification_property.notify_delay_after
    }
  }

  dynamic "execution_property" {
    for_each = var.glue_job_execution_property != null ? [true] : []
    content {
      max_concurrent_runs = var.glue_job_execution_property.max_concurrent_runs
    }
  }
  tags = var.tags
}

resource "aws_glue_trigger" "this" {
  count = var.create_glue_trigger ? 1 : 0

  name              = var.glue_trigger_name
  type              = var.glue_trigger_type
  schedule          = try(var.glue_trigger_schedule, null)
  enabled           = try(var.glue_trigger_enabled, null)
  start_on_creation = try(var.glue_trigger_type == "ON_DEMAND" ? false : var.glue_trigger_start_on_creation, null)

  dynamic "predicate" {
    for_each = var.glue_trigger_predicate != null ? [true] : []
    content {
      logical = try(var.glue_trigger_predicate.logical, null)
      dynamic "conditions" {
        for_each = var.glue_trigger_predicate.conditions
        content {
          job_name         = try(conditions.value.job_name, null)
          state            = try(conditions.value.state, null)
          crawler_name     = try(conditions.value.crawler_name, null)
          crawl_state      = try(conditions.value.crawl_state, null)
          logical_operator = try(conditions.value.logical_operator, null)
        }
      }
    }
  }
  dynamic "actions" {
    for_each = var.glue_trigger_actions

    content {
      job_name               = try(actions.value.job_name, null)
      crawler_name           = try(actions.value.crawler_name, null)
      arguments              = try(actions.value.arguments, null)
      security_configuration = try(actions.value.security_configuration, null)
      timeout                = try(actions.value.timeout, null)

      dynamic "notification_property" {
        for_each = try(actions.value.notification_property, null) != null ? [true] : []
        content {
          notify_delay_after = try(actions.value.notification_property.notify_delay_after, null)
        }
      }
    }
  }
  dynamic "event_batching_condition" {
    for_each = var.glue_trigger_event_batching_condition != null ? [true] : []

    content {
      batch_size   = var.glue_trigger_event_batching_condition.batch_size
      batch_window = try(var.glue_trigger_event_batching_condition.batch_window, null)
    }
  }
  tags = var.tags
}

resource "aws_glue_connection" "this" {
  count = var.create_glue_connection ? 1 : 0

  name                  = var.glue_connector_name
  description           = try(var.glue_connection_description, null)
  connection_type       = try(var.glue_connection_type, null)
  connection_properties = try(var.glue_connection_properties, null)
  catalog_id            = try(var.glue_catalog_id, null)
  match_criteria        = try(var.glue_match_criteria, null)

  dynamic "physical_connection_requirements" {
    for_each = var.glue_connection_network != null ? [true] : []
    content {
      availability_zone      = try(var.glue_connection_network.availability_zone, null)
      security_group_id_list = try(var.glue_connection_network.security_group_id_list, null)
      subnet_id              = try(var.glue_connection_network.subnet_id, null)
    }
  }

  tags = var.tags

}
