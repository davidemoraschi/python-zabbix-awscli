import requests
import json
import time
import pandas as pd
import numpy as np
import concurrent.futures
from io import StringIO 
import shutil
import os
import datetime
import dateutil.parser
# from gcpConnector import GcpConnector
from lib.common import Common
from lib.uidFromAccountSearch import get_uids



def fetch_data_getAccountInfo(uid: str, credentialFileCDC="credentialCDC.json", tries: int = 5) -> str:
    '''
    Return the query result from accounts.getAccountInfo table using one uid
    
        Args: 
            uid (str): The uid, e.g. '1_886218'
            tries (int): Define how many times for re-requery before araise an exception,
                the default value is 5
        
        Returns:
            str: the JSON query result in a string format
            
        Raises: Exception raises for server connection error, and the exception will be shown
        
    '''

    for tryN in range(tries):
      try: 
        URL, params, timeIdentifier, table = Common().get_cdc_connect(
            credentialFileCDC, "accounts.getAccountInfo"
        )
        params['uid'] = uid
        params['extraProfileFields'] = 'languages, address, phones, education, educationLevel, honors, publications,  patents, certifications, professionalHeadline, bio, industry, specialities, work, skills, religion, politicalView, interestedIn, relationshipStatus, hometown, favorites, followersCount, followingCount, username, name, locale, verified, timezone, likes, samlData.'
        params['include'] = 'identities-active , identities-all , identities-global , loginIDs , emails, profile, data, password, isLockedOut, lastLoginLocation, regSource, irank, rba, subscriptions, userInfo, preferences, groups'
        response = requests.get(URL, params = params)

      except Exception as e:
          if tryN <= tries:
            print(f"error: {e}")
            time.sleep(15)#retry after 15 sec
            continue
          else:
            raise Exception(f"{e}")
      break
    # logging("gogo")

    return json.dumps(response.json())

def _prepare_local_folders(dataPath):
    """prepare folders, only works when saveLocation = 'local'"""

    # delete the folder if exists, then create a new one
    if os.path.exists(dataPath):
        shutil.rmtree(dataPath)

    # os.makedirs(folderPath)
    os.makedirs(dataPath)

def main():
 
    start = '2021-02-26T10:35:26.135Z'
    # end = dateutil.parser.parse('2021-12-26T00:00:00.000Z')
    end = datetime.datetime.now(datetime.timezone.utc)
    end = Common().datetime2str(end)

    # bucketName = "bx5050-test1"
    # BucketCredentialFile = "straumann-global-a27d2a8d8096.json"
    credentialFileCDC = "credentialCDC.json"


    
    # 1. get all uids
    uids, uids_len = get_uids(start, end, credentialFileCDC)

    #2.use uids
    # split all the uids into several groups. In each group, the query is
    # performed concurrently, and the response data is save as
    # a JSON file.
    # uid_group = np.array_split(pd.read_csv("src/UIDs.csv").iloc[:,0].values, 1e3)
    uid_group = np.array_split(uids, 1e3)

    # locationObj = GcpConnector(
    #     bucketName,
    #     BucketCredentialFile
    # )
    # locationObj.delete_blob(folderPath)
    locationObj = None

    folderPath = f"Accounts_getAccountInfo-{start}---{end}"
    _prepare_local_folders(folderPath)

    num_cores = os.cpu_count()
    count = 0
    for partN, inputs in enumerate(uid_group):

      jsonFile_tem = ""
      
      with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
          inputs = [["credentialFileCDC", uid] for uid in inputs]
          results = [executor.submit(fetch_data_getAccountInfo, i) for i in inputs]
          for f in concurrent.futures.as_completed(results):
            jsonFile_tem += f"{f.result()},"
          count += len(results)
      print(
          f"part_{partN}. Obtained accounts.accountInfo lenth is {count}, total lenth: {uids_len}, {round(count/uids_len*100,6)}%")
      #output JSON file
      jsonFile = StringIO()
      jsonFile.write("[" + jsonFile_tem[:-1] + "]") 
      # save to local or GCP
      Common()._save_to_json(os.path.join(folderPath, f"part_{partN}"), jsonFile, None)
      # locationObj.write_json_to_gcp(os.path.join(folderPath,f"part_{partN}"), jsonFile)
      # jsonFile.close()





if __name__ == '__main__':
    main()