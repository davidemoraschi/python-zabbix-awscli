#!/usr/local/bin/python

# Copyright (C) 2001-2023 Zabbix SIA
#
# Zabbix SIA licenses this file to you under the MIT License.
# See the LICENSE file in the project root for more information.
"""Calls AWS AppFlow API to check for execution and returns the result to Zabbix"""

import json
import datetime
import boto3
from zabbix_utils import Sender


def serialize_datetime(obj):
    """Define a custom function to serialize datetime objects """
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


class FlowExecution:  # pylint: disable=too-few-public-methods
    """doc string"""

    def __init__(self, executionid: str, datapullendtime: datetime.datetime, executionstatus: str, recordsprocessed: int,
                 catalogstatus: str = '', catalogerror: str = '', partitionstatus: str = '', partitiongerror: str = ''):
        self.executionid = executionid
        self.datapullendtime = datapullendtime
        self.executionstatus = executionstatus
        self.recordsprocessed = recordsprocessed
        self.catalogstatus = catalogstatus
        self.catalogerror = catalogerror
        self.partitionstatus = partitionstatus
        self.partitiongerror = partitiongerror


client = boto3.client('appflow')
response = client.describe_flow_execution_records(
    flowName='github-to-s3',
    maxResults=1
)

flow_execution_result = FlowExecution(
    executionid=response['flowExecutions'][0]['executionId'],
    datapullendtime=response['flowExecutions'][0]['dataPullEndTime'],
    executionstatus=response['flowExecutions'][0]['executionStatus'],
    recordsprocessed=response['flowExecutions'][0]['executionResult']['recordsProcessed']
)

if 'metadataCatalogDetails' in response['flowExecutions'][0]:
    flow_execution_result.catalogstatus = response['flowExecutions'][0]['metadataCatalogDetails'][0]['tableRegistrationOutput']['status']
    flow_execution_result.catalogerror = response['flowExecutions'][0]['metadataCatalogDetails'][0]['tableRegistrationOutput']['message']
    flow_execution_result.partitionstatus = response['flowExecutions'][0]['metadataCatalogDetails'][0]['partitionRegistrationOutput']['status']
    flow_execution_result.partitiongerror = response['flowExecutions'][0]['metadataCatalogDetails'][0]['partitionRegistrationOutput']['message']

# Zabbix server/proxy details for Sender
# ZABBIX_SERVER = {
#     'server': 'zabbix-server',  # Zabbix server/proxy IP address or hostname
#     'port': 10051               # Zabbix server/proxy port for Sender
# }

# Create an instance of the Sender class with the specified server details
# sender = Sender(**ZABBIX_SERVER)
sender = Sender('zabbix-server')

# Send a value to a Zabbix server/proxy with specified parameters
# Parameters: (host, key, value, clock, ns)
responses = sender.send_value('zabbix-server', 'github-to-s3',
                              json.dumps(flow_execution_result.__dict__, default=serialize_datetime))

for node, resp in responses.items():
    # Check if the value sending was successful
    if resp.failed == 0:
        # Print a success message along with the response time
        print(f"Value sent successfully to {node} in {resp.time}")
    else:
        # Print a failure message
        print(f"Failed to send value to {node}")
