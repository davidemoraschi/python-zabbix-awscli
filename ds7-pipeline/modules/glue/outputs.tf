## glue catalog db

output "glue_catalog_db_id" {
  description = "Glue catalog database ID"
  value       = try(aws_glue_catalog_database.this[0].id,"")
}

output "glue_catalog_db_name" {
  description = "Glue catalog database name"
  value       = try(aws_glue_catalog_database.this[0].name,"")
}

output "glue_catalog_db_arn" {
  description = "Glue catalog database ARN"
  value       = try(aws_glue_catalog_database.this[0].arn,"")
}


## glue catalog table
# output "glue_catalog_table_id" {
#   description = "Glue catalog table ID"
#   value       = try(aws_glue_catalog_table.this[0].id,"")
# }

# output "glue_catalog_table_name" {
#   description = "Glue catalog table name"
#   value       = try(aws_glue_catalog_table.this[0].name,"")
# }

# output "glue_catalog_table_arn" {
#   description = "Glue catalog table ARN"
#   value       = try(aws_glue_catalog_table.this[0].arn,"")
# }


## glue crawler 
output "glue_crawler_id" {
  description = "Glue crawler ID"
  value       = try(aws_glue_crawler.this[0].id,"")
}

output "glue_crawler_name" {
  description = "Glue crawler name"
  value       = try(aws_glue_crawler.this[0].name,"")
}

output "glue_crawler_arn" {
  description = "Glue crawler ARN"
  value       = try(aws_glue_crawler.this[0].arn,"")
}


## glue_job 
output "glue_job_id" {
  description = "Glue job ID"
  value       = try(aws_glue_job.this[0].id, null)
}

output "glue_job_name" {
  description = "Glue job name"
  value       = try(aws_glue_job.this[0].name, null)
}

output "glue_job_arn" {
  description = "Glue job ARN"
  value       = try(aws_glue_job.this[0].arn, null)
}

output "glue_job_tags_all" {
  description = "A map of tags assigned to the resource, including those inherited from the provider default_tags configuration block."  
  value = try(aws_glue_job.this[0].tags_all, null)
}

## glue_connection
output "glue_connection_id" {
  description = "Glue connection ID"
  value       = try(aws_glue_connection.this[0].id,"")
}

output "glue_connection_tags_all" {
  description = "Glue connection tags all"
  value       = try(aws_glue_connection.this[0].tags_all,"")
}

output "glue_connection_arn" {
  description = "Glue connection ARN"
  value       = try(aws_glue_connection.this[0].arn,"")
}