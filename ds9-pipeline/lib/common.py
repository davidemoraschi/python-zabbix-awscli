import requests
import json
import pandas as pd
import datetime
import dateutil.parser
import time
import os
from io import StringIO
# from gcpConnector import GcpConnector
import argparse


class Common:
    '''
        Some common functions which could be used by other classed.
    '''

    def datetime_split(self, start: str, end: str, step=300) -> list:
        '''
        Split the datetime range [start, end] into step + 1 chunks

        Args:
            start(str): Start datetime
            end(str): End datetime
            step: Time interval

        Returns:
            list of datetime string with the given time interval

        Examples:
            >>> start = '2021-02-26T10:35:26.135Z'
            >>> end = '2021-12-28T00:00:00.000Z'
            >>> step = 2
            "['2021-02-26T10:35:26.135Z', '2021-07-28T17:17:43.067Z', '2021-12-28T00:00:00.000Z']"
        '''

        start = dateutil.parser.parse(start)
        end = dateutil.parser.parse(end)
        delta = (end - start)/step

        dayArray = [(start + delta*i).isoformat(timespec="milliseconds").replace("+00:00", "Z")
                    for i in range(step)]
        dayArray.append(end.isoformat(
            timespec="milliseconds").replace("+00:00", "Z"))
        return dayArray


    def get_dayArray(self, start:str, end:str, chunkNum = 5) -> list:
        """
        Prepare grouped timestamp. Split one day into 5 chunks. 
        By default, Return 5 chunks if the given time range is less
        than one day

        Args:
            start(str): start datetime
            end(str): end datetime
        
        Returns:
            list of datetime string containing at least 5 elements.


        """
        start = self.str2datetime(start)
        end = self.str2datetime(end)
        # split one day into 5 chunks
        step = ((end - start).days + 1) * chunkNum

        dayArray = self.datetime_split(
            self.datetime2str(start),
            self.datetime2str(end),
            step=step,
        )
        return dayArray
    
    def str2datetime(self, datetimeStr:str) -> datetime.datetime:
        ''''
        convert string into datetime
        '''
        return dateutil.parser.parse(datetimeStr)

    def datetime2str(self, dt: datetime.datetime) -> str:
        '''
        Convert datetime to string

        Args:
            dt(datetime): datetime

        Returns:
            The timestamp format is ISO 8601 in UTC ('yyyy'-'MM'-'dd'T'HH':'mm':'ss.fff'Z'). 
                For example, '2021-12-25T17:26:03.139Z'.

        '''
        return dt.isoformat(timespec="milliseconds").replace("+00:00", "Z")

    def fetch_data(self, t1: str, t2: str, URL: str, params: dict, table: str, timeIdentifier: str,
                   ) -> tuple[StringIO, str, bool]:
        '''
        Query data from the time range of [t1, t2). 

        Args: 
            t1(str): Start time
            t2(str): End time
            URL(str): Query url
            params(dict): Query parameters
            table(str): Database table
            timeIdentifier(str): Data field name used in WHERE clause
            # dataPath(str): Folder path for saving the resulting .json file

        Returns:
            jsonFile(StringIO): Query result in the form of in-memery file-like object
            writeCounter(str): Return total counts from this query
            isSuccessed(bool): True only when all the paginations are succeededly obtained
            # writeUids(list): All the uids obtained from this query
        Raises:
            Raise excpetion if 'errorCode' != 0

        Examples:
            >>> t1 = "2021-02-26T10:35:26.135Z" 
            >>> t2 = "2022-12-26T00:00:00.000Z"
            >>> URL = 'https://accounts.eu1.gigya.com/accounts.search'
            >>> params = {'apiKey':?, 'uerKey':?, 'secret':?}
            >>> table = "accounts"
            >>> timeIdentifier = "lastUpdated"
            # >>> dataPath = "account_search_data/data"
            >>> fetch_data_accounts_search(t1, t2, URL, params, table, timeIdentifier)

            StringIO-object, 2736000, True
        '''

        # output json file name
        saveJSON = StringIO()
        isSucceeded = False  # flag to show if all the paginations succeed


        nextCursorId = ''  # pagination
        writeCounter = 0  # total counts from this query
        while True:
            if nextCursorId == '':  # first query
                params['query'] = f"SELECT * FROM {table} WHERE ({timeIdentifier} >= '{t1}' and \
                    {timeIdentifier} < '{t2}') ORDER BY {timeIdentifier} LIMIT 2500"
                params['openCursor'] = 'true'
                if params.get('cursorId'):
                    params.pop('cursorId')
                # create the output file
                saveJSON.write('[')
            else:  # after first query
                params['cursorId'] = nextCursorId
                if params.get('query'):
                    params.pop('query')
                    params.pop('openCursor')

            # query
            response = requests.get(URL, params=params)
            queryResult = response.json()

            # error fetching data
            if queryResult.get('errorCode') != 0 or queryResult.get('results') is None:
                raise Exception(queryResult)

            # list of all records from this page
            tempOutput = queryResult.get('results')
            writeCounter += len(tempOutput)


            # check if the end of the result
            if queryResult.get('nextCursorId') is None:
                isSucceeded = True
                saveJSON.write(f"{json.dumps(tempOutput)[1:]}")
                break
            else:
                # remove the {} and add a comma
                saveJSON.write(f"{json.dumps(tempOutput)[1:-1]},")
                nextCursorId = queryResult['nextCursorId']

        # return obtained records from the time range of [t1, t2)
        return saveJSON, writeCounter, isSucceeded

    def _save_to_json(self, jsonPath: str, saveJSON: StringIO, locationObj: object):
        '''
        Save StringIO object to storage (local or server)

        Args:
            jsonPath(str): Folder path and json file name
            saveJSON(StringIO): In-memery file-like object
            # saveLocation(list): Place to save all .json files. Could be an element in ["local", "GCP_bucket"]

        '''
        if locationObj is None:
            with open(jsonPath, 'w') as f:
                f.write(saveJSON.getvalue())
        elif isinstance(locationObj, GcpConnector):  # google bucket
            locationObj.write_json_to_gcp(jsonPath, saveJSON)

        # free memory space
        saveJSON.close()

    def query_all_data(self, dayArray: list, URL: str, params: dict, table: str, timeIdentifier: str,
                       dataPath: str, locationObj: object = None) -> tuple[int, pd.DataFrame]:
        '''
        This function iterates the datetime listed in dayArray. For each iteration, it calls 
        'fetch_data()', and the query result will be saved into a file (with the filename 't1-t2.json')

        Args:
            dayArray: List of datetime string
            URL(str): Query url
            params(dict): Query parameters
            table(str): Database table
            timeIdentifier(str): Data field name used in WHERE clause
            dataPath(str): Relative folder path or blob name for saving the all .json files
            # saveLocation(list): Place to save all .json files. Could be an element in ["local", "GCP_bucket"]
            locationObj(object): object to write, read and list files in server. "None" means local

        Returns:
            totalWriteCounter(int): Whole count
            dfFormattedlog(pd.DataFrame): Used for output the 'formattedLog.csv' file

        '''
        totalWriteCounter = 0  # the whole count
        formattedlog = []
        tryN = 5 # try 5 times before exit with the Excpetion


        t1 = dayArray[0]
        for i, t2 in enumerate(dayArray[1:], 1):
            # self.logger.info(f"chunk {i}: {t1} - {t2}")
            for n in range(tryN):
                try:
                    saveJSON, count, isSucceeded = self.fetch_data(t1, t2,  URL, params, table,
                                                                timeIdentifier)
                except Exception as e:
                    if n < tryN:
                        time.sleep(10)
                        continue
                    else:
                        raise Exception(e)
                break

            # write query result to .json The query result will be saved
            # into a file (with the filename 't1-t2.json')
            jsonPath = os.path.join(
                dataPath, f"{t1.replace(':','.')}_{t2.replace(':','.')}.json")
            self._save_to_json(jsonPath, saveJSON, locationObj)

            totalWriteCounter += count  # add count
            formattedlog.append([t1, t2, count, isSucceeded])
            t1 = t2
        columns = ["start_time", "end_time", "count", "is_succeeded"]
        dfFormattedlog = pd.DataFrame(formattedlog, columns=columns)
        return totalWriteCounter, dfFormattedlog

    def get_cdc_connect(self, credentialFileCDC:str, tableKey:str):
        """credentials and query parameters to access CDC"""
        # credentials to access CDC
        with open(credentialFileCDC) as f:
            cre = pd.json_normalize(json.load(f))
        URL = cre.iloc[0][f"{tableKey}.URL"]
        params = {}
        params["secret"] = cre.iloc[0]["secret"]
        params["userKey"] = cre.iloc[0]["userKey"]
        params["apiKey"] = cre.iloc[0]["apiKey"]
        timeIdentifier = cre.iloc[0][f"{tableKey}.timeIdentifier"]
        table = cre.iloc[0][f"{tableKey}.table"]

        return URL, params, timeIdentifier, table
