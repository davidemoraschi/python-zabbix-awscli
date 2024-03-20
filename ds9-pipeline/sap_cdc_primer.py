#!/usr/bin/python
'''
Testing the GSSDK
'''
import json
from typing import Dict

import requests
import GSSDK

APIKEY = '3_sUuYY3aPXsYTusEqibJXwme9HwNRxM-N3_Wx2Z4HV3X47ft6BZY-JzcA2kBMaPcy'
SECRETKEY = '2lm93KoFJBKPvrKfdc5qFx5oqcbx5TcX'
USERKEY = 'ADwPPFXaaoAn'

def get_headers() -> Dict[str, str]:
    '''Returns the headers for the API requests'''
    # token = retrieve_access_token()
    return {"Content-Type": "application/x-www-form-urlencoded"}

headers: Dict[str, str] = get_headers()

# Construct API URL
url: str = f'https://accounts.eu1.gigya.com/accounts.search?apiKey=3_sUuYY3aPXsYTusEqibJXwme9HwNRxM-N3_Wx2Z4HV3X47ft6BZY-JzcA2kBMaPcy&userKey=ADwPPFXaaoAn&secret=2lm93KoFJBKPvrKfdc5qFx5oqcbx5TcX&query=SELECT%20UID%20AS%20i%20FROM%20accounts%20limit%2010000&timeout=60000&context=awsglue&httpStatusCodes=true&openCursor=true'

# Make API request
response: requests.Response = requests.post(url=url, headers=headers)

# Raise an exception for bad status codes
response.raise_for_status()

result=json.loads(response.text)

print(result['objectsCount'])
