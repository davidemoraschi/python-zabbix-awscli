output "connector_arn" {
  description = "ARN of the connector profile."
  value       = aws_appflow_connector_profile.this.arn
}

output "connector_credentials_arn" {
  description = "ARN of the connector profile credentials."
  value       = aws_appflow_connector_profile.this.credentials_arn
}
