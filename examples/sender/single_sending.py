# Copyright (C) 2001-2023 Zabbix SIA
#
# Zabbix SIA licenses this file to you under the MIT License.
# See the LICENSE file in the project root for more information.

from zabbix_utils import Sender
import boto3
import json

class flow_execution:
    def __init__(self, id, executionstatus, catalogstatus, catalogerror):
        self.id = id
        self.executionstatus = executionstatus
        self.catalogstatus = catalogstatus
        self.catalogerror = catalogerror

client = boto3.client('appflow')
response = client.describe_flow_execution_records(
    flowName='github-to-s3',
    maxResults=1
)

flow_execution_result = flow_execution(
    response.get('flowExecutions')[0].get('executionId'),
    response.get('flowExecutions')[0].get('executionStatus'),
    response.get('flowExecutions')[0].get('metadataCatalogDetails')[0].get('tableRegistrationOutput').get('status'),
    response.get('flowExecutions')[0].get('metadataCatalogDetails')[0].get('tableRegistrationOutput').get('message')
)

# Zabbix server/proxy details for Sender
ZABBIX_SERVER = {
    "server": "zabbix-server",  # Zabbix server/proxy IP address or hostname
    "port": 10051               # Zabbix server/proxy port for Sender
}

# Create an instance of the Sender class with the specified server details
sender = Sender(**ZABBIX_SERVER)

# Send a value to a Zabbix server/proxy with specified parameters
# Parameters: (host, key, value, clock, ns)
responses = sender.send_value('zabbix-server', 'github-to-s3', json.dumps(flow_execution_result.__dict__))

for node, resp in responses.items():
    # Check if the value sending was successful
    if resp.failed == 0:
        # Print a success message along with the response time
        print(f"Value sent successfully to {node} in {resp.time}")
    else:
        # Print a failure message
        print(f"Failed to send value to {node}")
