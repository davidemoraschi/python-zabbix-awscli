rem @echo off

rem C:\cmder\bin\terraform import aws_appflow_flow.SAP_MKTCloud_AWSWEBREGFORM_CDS_Full arn:aws:appflow:eu-west-1:816247855850:flow/SAP_MKTCloud_AWSWEBREGFORM_CDS_Full
C:\cmder\bin\terraform plan -generate-config-out=generated.out

rem 1. Create the object in the AWS console and add to main.tf the following lines:
rem  # import {
rem  #   to = aws_appflow_flow.SAP_MKTCloud_AWSWEBREGFORM_CDS_Full
rem  #   id = "arn:aws:appflow:eu-west-1:816247855850:flow/SAP_MKTCloud_AWSWEBREGFORM_CDS_Full"
rem  # }
rem 2. Run terraform plan -generate-config-out=generated.out
rem 3. Copy the content to the main.tf file
rem 4. Comment the import node in main.tf and run terraform import
