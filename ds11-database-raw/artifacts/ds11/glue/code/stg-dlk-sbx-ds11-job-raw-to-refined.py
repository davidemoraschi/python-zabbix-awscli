#!/usr/bin/python
'''
# Python Shell jobs on AWS Glue:
# 1. Looks for SQL files in the folder specified in AWS_FOLDER
# 2. Executes them in alphabetical order
# 3. Outputs the row number of result set if any
# davide.moraschi@toptal.com 2024
'''

# Import necessary modules
import time
from tabulate import tabulate
from common_functions import log, log_environment, process_arguments, send_sns, execute_s3_sql_files_athena
from typing import Dict

# Process command line arguments
args: Dict[str, str] = process_arguments(options=['WORKFLOW_NAME', 'WORKFLOW_RUN_ID'])

# Print arguments for debugging
print(tabulate(tabular_data=args.items(), headers=['args.keys()', 'args.values()'], tablefmt='psql', showindex=False))

# Parse report IDs, workflow name, EVENT_TYPES, and job name from arguments
WORKFLOW_NAME: str = args['WORKFLOW_NAME']
WORKFLOW_RUN_ID: str = args['WORKFLOW_RUN_ID']
JOB_NAME: str = args['JOB_NAME'] if 'JOB_NAME' in args else 'stg-dlk-sbx-ds11-job-raw-to-refined'
JOB_RUN_ID: int = int(time.time())


def main():
    '''Main function'''

    try:
        # Log environment information for debugging
        log_environment()

        # Log start of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message='start-job')
        
        execute_s3_sql_files_athena(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID))

        # Log end of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message='end-job')
   
    except Exception as exc:
        # Log error
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message=f'An error occurred:{str(exc)}')

        # Send SNS notification of error
        send_sns(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
                 job_run_id=str(JOB_RUN_ID), exc=exc)

        # Log end of job
        log(workflow_name=WORKFLOW_NAME, workflow_run_id=WORKFLOW_RUN_ID, job_name=JOB_NAME,
            job_run_id=str(JOB_RUN_ID), str_message='end-job')

        # Reraise exception
        # sys.exit(1)
        raise


# Run main function if script is run directly
if __name__ == "__main__":
    main()
    # sys.exit(0)
