#!/usr/local/bin/python
'''
#
# Copyright (C) 2024 Davide Moraschi (davide.moraschi@toptal.com)
# Invokes the AWS API get_job_runs to retrieve the last execution, status, cost and error if any 
# of all Glue Jobs in the region/profile passed as arguments
#
'''

import sys
import boto3
from classes.GlueJobExecution import GlueJobExecution
from zabbix_utils import Sender


def sort_jobexecution(gluejob):
    '''Return the completion date for sorting the list'''
    if gluejob.jobrunstate != 'RUNNING':
        return str(gluejob.completedon.isoformat())
    else:
        return '9999'


def send_to_zabbix(gluejobexecution):
    '''If a Zabbix server is available sends the JSON payload to it'''
    json_return_list: list = []

    for gluejob in gluejobexecution:
        json_return_list.append(gluejob.tojson().replace("'", ""))

    print(str(json_return_list).replace("'", ""))
    # Create an instance of the Sender class with the specified server details
    # sender = Sender(**ZABBIX_SERVER)
    sender = Sender('zabbix-server')
    # Send a value to a Zabbix server/proxy with specified parameters
    # Parameters: (host, key, value, clock, ns)
    responses = sender.send_value('zabbix-server', 'github-to-s3',
                                  str(json_return_list).replace("'", ""))
    for node, resp in responses.items():
        # Check if the value sending was successful
        if resp.failed == 0:
            # Print a success message along with the response time
            print(f"Value sent successfully to {node} in {resp.time}")
        else:
            # Print a failure message
            print(f"Failed to send value to {node}")


def pretty_print(gluejobexecution):
    '''Display results on screen'''
    print('Glue Job                                                - Last Status          Last Execution Date                Duration in Sec.       Cost in USD  Error')
    print(''.center(220, '-'))

    gluejobexecution.sort(reverse=True, key=sort_jobexecution)

    for gluejob in gluejobexecution:
        run_cost = round(0.44*max(gluejob.executiontime, 60)*gluejob.maxcapacity/(60*60), 2)
        if gluejob.jobrunstate == 'RUNNING':
            completed_on = '--'
        else:
            completed_on = gluejob.completedon.isoformat()
        print(
            f'{gluejob.jobname:55} - {gluejob.jobrunstate:20} {completed_on:40} {gluejob.executiontime:10} {run_cost:15} $  {gluejob.errormessage[:60]:60}')
    print(''.center(220, '-'))


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
            if 'ErrorMessage' in response['JobRuns'][0].keys():
                errormessage = response['JobRuns'][0]['ErrorMessage']
            else:
                errormessage = ''
            if response['JobRuns'][0]['JobRunState'] == 'RUNNING':
                completedon = '--'
            else:
                completedon = response['JobRuns'][0]['CompletedOn']

            gluejobexecution.append(GlueJobExecution(
                jobname=response['JobRuns'][0]['JobName'],
                jobrunid=response['JobRuns'][0]['Id'],
                jobrunstate=response['JobRuns'][0]['JobRunState'],
                startedon=response['JobRuns'][0]['StartedOn'],
                completedon=completedon,
                executiontime=response['JobRuns'][0]['ExecutionTime'],
                maxcapacity=response['JobRuns'][0]['MaxCapacity'],
                errormessage=errormessage)
            )

    pretty_print(gluejobexecution)
    # send_to_zabbix(gluejobexecution)


if __name__ == "__main__":
    main()
