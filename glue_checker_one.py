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
    if gluejob.completedon != '--':
        return str(gluejob.completedon.isoformat())
    return '9999'


def send_to_zabbix(gluejobexecution, jobname):
    '''If a Zabbix server is available sends the JSON payload to it'''
    json_return_list: list = []

    for gluejob in gluejobexecution:
        json_return_list.append(gluejob.tojson().replace("'", ""))

    # print(str(json_return_list).replace("'", ""))
    # Create an instance of the Sender class with the specified server details
    # sender = Sender(**ZABBIX_SERVER)
    sender = Sender('zabbix-server')
    # Send a value to a Zabbix server/proxy with specified parameters
    # Parameters: (host, key, value, clock, ns)
    responses = sender.send_value(jobname, 'aws-glue-job-result',
                                  str(json_return_list).replace("'", ""))
    
    # print(f'job-result-{jobname}')
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
    print('Glue Job                                                - Last Status          Last Execution Date                Duration in Sec.       Cost in USD  Error')  # pylint: disable=line-too-long
    print(''.center(220, '-'))

    gluejobexecution.sort(reverse=True, key=sort_jobexecution)

    for gluejob in gluejobexecution:
        run_cost = round(0.44*max(gluejob.executiontime, 60)*gluejob.maxcapacity/(60*60), 2)
        if gluejob.completedon == '--':
            completed_on = '--'
        else:
            completed_on = gluejob.completedon.isoformat()
        print(
            f'{gluejob.jobname:55} - {gluejob.jobrunstate:20} {completed_on:40} {gluejob.executiontime:10} {run_cost:15} $  {gluejob.errormessage[:60]:60}')  # pylint: disable=line-too-long
    print(''.center(220, '-'))


def main():
    '''Main function'''

    joblist: list = []

    profile_session = boto3.Session(region_name=str(sys.argv[1]), profile_name=str(sys.argv[2]))
    jobname:str = str(sys.argv[3])
    client = profile_session.client(service_name='glue')
    #response = client.get_jobs(MaxResults=1000)

    # for element in response['Jobs']:
    joblist.append(jobname)

    gluejobexecution = []
    for job in joblist:
        response = client.get_job_runs(JobName=job, MaxResults=1)       #type: ignore
        if response['JobRuns']:                                         #type: ignore   

            if 'ErrorMessage' in response['JobRuns'][0].keys():         #type: ignore
                errormessage = response['JobRuns'][0]['ErrorMessage']   #type: ignore
            else:
                errormessage = ''
            if 'CompletedOn' in response['JobRuns'][0].keys():          #type: ignore
                completedon = response['JobRuns'][0]['CompletedOn']     #type: ignore
            else:
                if response['JobRuns'][0]['ExecutionTime'] == 0:        #type: ignore
                    completedon = response['JobRuns'][0]['StartedOn']   #type: ignore
                else:
                    completedon = '--'                                  #type: ignore

            gluejobexecution.append(GlueJobExecution(
                jobname=response['JobRuns'][0]['JobName'],              #type: ignore
                jobrunid=response['JobRuns'][0]['Id'],                  #type: ignore
                jobrunstate=response['JobRuns'][0]['JobRunState'],      #type: ignore
                startedon=response['JobRuns'][0]['StartedOn'],          #type: ignore
                completedon=completedon,
                executiontime=response['JobRuns'][0]['ExecutionTime'],  #type: ignore
                maxcapacity=response['JobRuns'][0]['MaxCapacity'],      #type: ignore
                errormessage=errormessage)
            )

    #pretty_print(gluejobexecution)
    send_to_zabbix(gluejobexecution, jobname)


if __name__ == "__main__":
    main()
