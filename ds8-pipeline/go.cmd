@echo off

C:\cmder\bin\terraform plan -detailed-exitcode -out tfplan
IF %ERRORLEVEL% EQU 2 C:\cmder\bin\terraform apply -auto-approve
rem IF %ERRORLEVEL% EQU 0 aws glue start-job-run --job-name stg-dlk-sbx-ds14-job-source-to-raw --profile 816247855850_AdministratorAccess
rem IF %ERRORLEVEL% EQU 0 aws glue start-job-run --job-name stg-dlk-sbx-ds14-job-raw-to-refined --profile 816247855850_AdministratorAccess
rem IF %ERRORLEVEL% EQU 0 aws glue start-workflow-run --name ds14_pipeline --profile 816247855850_AdministratorAccess
