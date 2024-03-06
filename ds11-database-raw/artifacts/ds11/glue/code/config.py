'''Constants for the Glue Job'''

AWS_REGION              = 'eu-west-1'
AWS_BUCKET              = 'stg-dlk-sbx-ds-11-ext'
AWS_FOLDER              = 'events_feed/events_jsonl/'
AWS_ATHENA_DATABASE     = 'stg-dlk-sbx-ds11-raw-db'
AWS_ATHENA_OUPUT        = 's3://stg-dlk-sbx-ds-11-raw'
AWS_PROFILE             = ''
AWS_SECRET_NAME         = 'glue_job_sftp_data_catalog'
S3_DESTINATION_BUCKET   = 'stg-dlk-sbx-ds-11-raw'
S3_DESTINATION_PATH     = 'events_feed/events_jsonl_gzip/'
S3_PROCESSED_FOLDER     = 'events_feed_processed/'
SNS_FAILURE_TOPIC       = 'arn:aws:sns:eu-west-1:816247855850:ds11-failure-topic'