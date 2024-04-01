#!/usr/bin/python
'''
Testing the SAP CDC API to get the audit logs
'''

import awswrangler as wr
DEBUG:bool = True

database_name:str = 'stg-dlk-sbx-ds9-raw-db'
sql_query:str = '''INSERT INTO sapcdc_etl_log(bigint_epoch_ts_log,str_glue_job_name,str_glue_job_step,bigint_rows_retrieved,str_error_message) 
                    VALUES(to_unixtime(current_timestamp),:str_glue_job_name;,:str_glue_job_step;,:bigint_rows_retrieved;,:str_error_message;)'''

get_query_execution:dict = wr.athena.start_query_execution(sql=sql_query,
                                                           database=database_name,
                                                           params={
                                                               "str_glue_job_name": "'job_name_python'",
                                                               "str_glue_job_step": "'job_step_python'",
                                                               "bigint_rows_retrieved": 0,
                                                               "str_error_message":"'all good'"
                                                           },
                                                           wait=True)

if DEBUG:
    print(f'{get_query_execution["Status"]["State"]} in {get_query_execution["Statistics"]["TotalExecutionTimeInMillis"]}ms')
