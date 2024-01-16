#!/usr/local/bin/python
'''
# Copyright (C) 2001-2023 Zabbix SIA
#
# Zabbix SIA licenses this file to you under the MIT License.
# See the LICENSE file in the project root for more information.
# Calls AWS AppFlow API to check for execution and returns the result to Zabbix
'''

import json
import datetime

class GlueJobExecution:
    '''class to hold results from AWS API calls'''

    def __init__(self, jobrunid: str, jobrunstate: str,  # pylint: disable=too-many-arguments
                 startedon: datetime.datetime, completedon: datetime.datetime, executiontime: int):
        self.jobrunid = jobrunid
        self.jobrunstate = jobrunstate
        self.startedon = startedon
        self.completedon = completedon
        self.executiontime = executiontime

    def serialize_datetime(self, obj):
        '''Define a custom function to serialize datetime objects'''
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def tojson(self):
        '''returns json representation of content'''
        return json.dumps(self.__dict__, default=self.serialize_datetime)
