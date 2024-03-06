'''Constants for the Glue Job'''

# AWS_SECRET_NAME       = 'glue_job_sftp_data_catalog'
# S3_DESTINATION_BUCKET = 'stg-dlk-sbx-ds-11-raw'
# S3_DESTINATION_PATH = 'events_feed/events_jsonl_gzip/'
# S3_PROCESSED_FOLDER = 'events_feed_processed/'

AWS_REGION              = 'eu-west-1'
AWS_BUCKET              = 'stg-dlk-sbx-code-artifacts'
AWS_FOLDER              = 'artifacts/glue_job_ds6/sql/'
AWS_SECRET_NAME         = 'stg/dlk/docebo/ds6/secrets'
AWS_ATHENA_DATABASE     = 'stg-dlk-sbx-ds6-raw-db'
AWS_ATHENA_OUPUT        = 's3://stg-dlk-sbx-ds-6-raw'
AWS_PROFILE             = ''
# FTP_FOLDER              = '/data/feed'
# FTP_FILE_PATTERN        = 'products_feed_*.gz'
S3_BUCKET               = 'stg-dlk-sbx-ds-6-raw'
S3_PATH                 = 'docebo_feed/reports_csv_gzip/'
SNS_FAILURE_TOPIC       = 'arn:aws:sns:eu-west-1:816247855850:ds6-failure-topic'