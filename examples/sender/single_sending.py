# Copyright (C) 2001-2023 Zabbix SIA
#
# Zabbix SIA licenses this file to you under the MIT License.
# See the LICENSE file in the project root for more information.
"""Calls AWS AppFlow API to check for execution and returns the result to Zabbix"""

import json
import boto3

from zabbix_utils import Sender


class FlowExecution: # pylint: disable=too-few-public-methods
    """doc string"""
    def __init__(self, executionid: int, executionstatus: str, catalogstatus: str, catalogerror: str):
        self.executionid = executionid
        self.executionstatus = executionstatus
        self.catalogstatus = catalogstatus
        self.catalogerror = catalogerror

client = boto3.client('appflow')
response = client.describe_flow_execution_records(
    flowName='github-to-s3',
    maxResults=1
)

flow_execution_result = FlowExecution(
    executionid=response.get('flowExecutions')[0].get('executionId'),
    executionstatus=response.get('flowExecutions')[0].get('executionStatus'),
    catalogstatus=response.get('flowExecutions')[0].get('metadataCatalogDetails')[0].get('tableRegistrationOutput').get('status'),
    catalogerror=response.get('flowExecutions')[0].get('metadataCatalogDetails')[0].get('tableRegistrationOutput').get('message')
)

# Zabbix server/proxy details for Sender
ZABBIX_SERVER = {
    "server": "zabbix-server",  # Zabbix server/proxy IP address or hostname
    "port": 10051           # Zabbix server/proxy port for Sender
}

# Create an instance of the Sender class with the specified server details
sender = Sender(**ZABBIX_SERVER)

# Send a value to a Zabbix server/proxy with specified parameters
# Parameters: (host, key, value, clock, ns)
responses = sender.send_value('zabbix-server', 'github-to-s3',
                              json.dumps(flow_execution_result.__dict__))

for node, resp in responses.items():
    # Check if the value sending was successful
    if resp.failed == 0:
        # Print a success message along with the response time
        print(f"Value sent successfully to {node} in {resp.time}")
    else:
        # Print a failure message
        print(f"Failed to send value to {node}")
