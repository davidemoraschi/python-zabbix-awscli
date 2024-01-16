#!/usr/local/bin/python
'''
# Copyright (C) 2001-2023 Zabbix SIA
#
# Zabbix SIA licenses this file to you under the MIT License.
# See the LICENSE file in the project root for more information.
# Calls AWS AppFlow API to check for execution and returns the result to Zabbix
'''

import sys
import boto3
from classes.GlueJobExecution import GlueJobExecution
from zabbix_utils import Sender as zabbix_sender


def main():
    '''Main function'''
    jobname: str = str(sys.argv[1])

    client = boto3.client('glue')
    response = client.get_job_runs(JobName=jobname, MaxResults=1)

    gluejobexecution: GlueJobExecution = GlueJobExecution(
        jobrunid=response['JobRuns'][0]['Id'],
        jobrunstate=response['JobRuns'][0]['JobRunState'],
        startedon=response['JobRuns'][0]['StartedOn'],
        completedon=response['JobRuns'][0]['CompletedOn'],
        executiontime=response['JobRuns'][0]['ExecutionTime']
    )

    zabbixsender = zabbix_sender('zabbix-server')
    ret = zabbixsender.send_value('zabbix-server', jobname, gluejobexecution.tojson())

    for node, resp in ret.items():
        if resp.failed == 0:
            print(f"Value sent successfully to {node} in {resp.time}")
        else:
            print(f"Failed to send value to {node}")


if __name__ == "__main__":
    main()
