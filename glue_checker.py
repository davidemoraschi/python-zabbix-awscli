#!/usr/local/bin/python
'''
#
# Copyright (C) 2024 Davide Moraschi (davide.moraschi@toptal.com)
#
'''

import sys
import boto3
from classes.GlueJobExecution import GlueJobExecution
# from zabbix_utils import Sender as zabbix_sender


def sort_jobexecution(gluejob):
    '''Return the completion date for sorting the list'''
    return gluejob.completedon.isoformat()


def main():
    '''Main function'''
    joblist: list = []
    jobname: str = str(sys.argv[1])

    client = boto3.client('glue')
    if jobname == '*':
        response = client.get_jobs(MaxResults=1000)
        for element in response['Jobs']:
            joblist.append(element['Name'])
    else:
        joblist.append(jobname)

    gluejobexecution: GlueJobExecution = []
    for job in joblist:
        response = client.get_job_runs(JobName=job, MaxResults=1)
        gluejobexecution.append(GlueJobExecution(
            jobname=response['JobRuns'][0]['JobName'],
            jobrunid=response['JobRuns'][0]['Id'],
            jobrunstate=response['JobRuns'][0]['JobRunState'],
            startedon=response['JobRuns'][0]['StartedOn'],
            completedon=response['JobRuns'][0]['CompletedOn'],
            executiontime=response['JobRuns'][0]['ExecutionTime'])
        )

    print(f'Glue Job                       - Last Status          Last Execution Date                Duration in Sec.')
    print(''.center(105, '-'))

    gluejobexecution.sort(reverse=True, key=sort_jobexecution)

    for gluejob in gluejobexecution:
        print(f'{gluejob.jobname:30} - {gluejob.jobrunstate:20} {gluejob.completedon.isoformat():40} {gluejob.executiontime:10}')
    print(''.center(105, '-'))

    # zabbixsender = zabbix_sender('zabbix-server')
    # ret = zabbixsender.send_value('zabbix-server', jobname, gluejobexecution.tojson())

    # for node, resp in ret.items():
    #     if resp.failed == 0:
    #         print(f"Value sent successfully to {node} in {resp.time}")
    #     else:
    #         print(f"Failed to send value to {node}")


if __name__ == "__main__":
    main()
