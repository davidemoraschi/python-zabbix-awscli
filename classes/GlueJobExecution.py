#!/usr/local/bin/python
'''
#
# Copyright (C) 2024 Davide Moraschi (davide.moraschi@toptal.com)
# Common class to retrieve Glue Job details from AWS API
#
'''

import json
import datetime
import time


class GlueJobExecution:
    '''class to hold results from AWS API calls'''

    def __init__(self, jobname: str, jobrunid: str, jobrunstate: str,  # pylint: disable=too-many-arguments
                 startedon: datetime.datetime, completedon: datetime.datetime, executiontime: int,
                 maxcapacity: int,
                 errormessage: str):
        self.jobname = jobname
        self.jobrunid = jobrunid
        self.jobrunstate = jobrunstate
        self.startedon = startedon
        self.completedon = completedon
        self.executiontime = executiontime
        self.errormessage = errormessage
        self.maxcapacity = maxcapacity
        self._ts = time.time()

    def serialize_datetime(self, obj):
        '''Define a custom function to serialize datetime objects'''
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def tojson(self):
        '''returns json representation of content'''
        return json.dumps(self.__dict__, default=self.serialize_datetime)
