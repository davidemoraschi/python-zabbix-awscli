import requests
import json
import time
import pandas as pd
import numpy as np
import concurrent.futures
from io import StringIO
import os
import datetime
import dateutil.parser
import logging
# from gcpConnector import GcpConnector
from lib.common import Common

def get_uids(start:str, end:str, credentialFileCDC:str):
    logging.getLogger().setLevel(logging.INFO)
    num_cores = os.cpu_count()
    #1. get all uids
    step = 30  # time interval

    # end = start + datetime.timedelta(days=31)
    logging.info(f"======{start}------{end}======")
    start = Common().str2datetime(start)
    end = Common().str2datetime(end)

    delta = (end - start)/step

    dayArray = [(start + delta*i).isoformat(timespec="milliseconds").replace("+00:00", "Z")
                for i in range(step)]
    dayArray.append(end.isoformat(
        timespec="milliseconds").replace("+00:00", "Z"))


    URL, params, timeIdentifier, table = Common().get_cdc_connect(
        credentialFileCDC, "account.search"
    )

    inputs = [d+[URL, params, table, timeIdentifier]
              for d in set_para(dayArray)]

    #fetch account.search table to get all uids
    uids_len = get_all_uid_lenth(URL, params)
    uids = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
        results = [executor.submit(fetch_data, *i) for i in inputs]
        for f in concurrent.futures.as_completed(results):
            uids += f.result()
            logging.info(f"obtained uid lenth: {len(uids)}, total lenth: {uids_len}, obtained {round(len(uids)/uids_len*100,6)}%")

    if len(uids) != uids_len:
      raise Exception(
          f"obtained uid lenth: {len(uids)}, but total lenth {uids_len}")
    else:
      logging.info(f"======================total {len(uids)} uids are obtained=========================")
    
    return uids, uids_len

def get_all_uid_lenth(URL, params: dict):
    for tryN in range(5):
      try:
        # URL = 'https://accounts.eu1.gigya.com/accounts.search'
        # params = {}
        # params['apiKey'] = '3_sUuYY3aPXsYTusEqibJXwme9HwNRxM-N3_Wx2Z4HV3X47ft6BZY-JzcA2kBMaPcy'
        # params['userKey'] = 'ADwPPFXaaoAn'
        # params['secret'] = '2lm93KoFJBKPvrKfdc5qFx5oqcbx5TcX'
        params['query'] = 'SELECT UID FROM accounts'
        # query
        response = requests.get(URL, params=params)
        queryResult = response.json()['totalCount']
      except Exception as e:
        if tryN < 5:
          time.sleep(5)
          continue
        else:
          Exception(f"{e}")
        break
    return queryResult
    

        
def set_para(dayArray):
    tList = []
    t1 = dayArray[0]
    for t2 in dayArray[1:]:
        tList.append([t1, t2])
        t1 = t2
    return tList


def fetch_data(t1: str, t2: str, URL: str, params: dict, table: str, timeIdentifier: str
               ) -> list:
    '''
    Query data from the time range of [t1, t2). The query result will be saved
        into a file (with the filename 't1-t2.json')
    
    Args: 
        t1(str): Start time
        t2(str): End time
        URL(str): Query url
        params(dict): Query parameters
        table(str): Database table
        # timeIdentifier(str): Data field name used in WHERE clause
        # dataPath(str): Folder path for saving the resulting .json file
    
    Returns:
        # writeCounter(str): Return total counts from this query
        # isSuccessed(bool): True only when all the paginations are succeededly obtained
        # writeUids(list): All the uids obtained from this query
    Raises:
        Raise excpetion if 'errorCode' != 0
        
    Examples:
        >>> t1 = "2021-02-26T10:35:26.135Z" 
        >>> t2 = "2022-12-26T00:00:00.000Z"
        >>> URL = 'https://accounts.eu1.gigya.com/accounts.search'
        >>> params = {'apiKey':?, 'uerKey':?, 'secret':?}
        >>> table = "accounts"
        # >>> timeIdentifier = "lastUpdated"
        # >>> dataPath = "account_search_data/data"
        >>> fetch_data_accounts_search(t1, t2, URL, params, table, timeIdentifier)
        
        ["1_886218", "1_972706"]
    '''

    nextCursorId = ''  # pagination
    writeUID = []  # list of uids form this query
    while True:
      if nextCursorId == '':  # first query
        params['query'] = f"SELECT UID FROM {table} WHERE ({timeIdentifier} >= '{t1}' and \
            {timeIdentifier} < '{t2}') LIMIT 2500"
        params['openCursor'] = 'true'
        if params.get('cursorId'):
            params.pop('cursorId')

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
        logging.info(params)
        raise Exception(queryResult)

      # list of all records from this page
      tempOutput = queryResult.get('results')

      if len(tempOutput) != 0:
        writeUID += pd.json_normalize(tempOutput)["UID"].tolist()


      # check if the end of the result
      # # the query is secceed
      if queryResult.get('nextCursorId') is None:
        break
      else:
        nextCursorId = queryResult['nextCursorId']

    # return obtained UIDs from the time range of [t1, t2)
    return writeUID