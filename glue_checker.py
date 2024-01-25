#!/usr/local/bin/python
'''
#
# Copyright (C) 2024 Davide Moraschi (davide.moraschi@toptal.com)
#
'''

import sys
import boto3
from classes.GlueJobExecution import GlueJobExecution


def sort_jobexecution(gluejob):
    '''Return the completion date for sorting the list'''
    return gluejob.completedon.isoformat()


def main():
    '''Main function'''

    joblist: list = []

    eu_west_1_session = boto3.Session(region_name=str(sys.argv[1]), profile_name=str(sys.argv[2]))
    client = eu_west_1_session.client(service_name='glue')
    response = client.get_jobs(MaxResults=1000)

    for element in response['Jobs']:
        joblist.append(element['Name'])

    gluejobexecution: GlueJobExecution = []
    for job in joblist:
        response = client.get_job_runs(JobName=job, MaxResults=1)
        if response['JobRuns']:
            gluejobexecution.append(GlueJobExecution(
                jobname=response['JobRuns'][0]['JobName'],
                jobrunid=response['JobRuns'][0]['Id'],
                jobrunstate=response['JobRuns'][0]['JobRunState'],
                startedon=response['JobRuns'][0]['StartedOn'],
                completedon=response['JobRuns'][0]['CompletedOn'],
                executiontime=response['JobRuns'][0]['ExecutionTime'])
            )
        else:
            print(f"Empry result: {job}")

    print('Glue Job                                                - Last Status          Last Execution Date                Duration in Sec.')
    print(''.center(105, '-'))

    gluejobexecution.sort(reverse=True, key=sort_jobexecution)

    for gluejob in gluejobexecution:
        print(f'{gluejob.jobname:55} - {gluejob.jobrunstate:20} {gluejob.completedon.isoformat():40} {gluejob.executiontime:10}')
    print(''.center(105, '-'))


if __name__ == "__main__":
    main()
