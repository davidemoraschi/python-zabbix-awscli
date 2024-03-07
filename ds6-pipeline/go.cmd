@echo off

C:\cmder\bin\terraform plan -detailed-exitcode -out tfplan
IF %ERRORLEVEL% EQU 2 C:\cmder\bin\terraform apply -auto-approve
rem IF %ERRORLEVEL% EQU 0 aws stepfunctions start-execution --state-machine-arn "arn:aws:states:eu-west-1:816247855850:stateMachine:stg-dlk-sbx-ds6-raw-sfn-new-report" ^
rem 
rem                                                        --profile 816247855850_AdministratorAccess

IF %ERRORLEVEL% EQU 0 aws glue start-workflow-run --name ds6_pipeline --profile 816247855850_AdministratorAccess
