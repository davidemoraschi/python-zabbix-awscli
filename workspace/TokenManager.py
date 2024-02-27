#!/usr/local/bin/python
'''
#
# Copyright (C) 2024 Davide Moraschi (davide.moraschi@toptal.com)
# Class to retrieve access token only if expired
#
'''

from datetime import datetime, timedelta
import json
import requests


class TokenManager:
    '''Boa Constructor.'''

    def __init__(self, token_url, credentials, refresh_token):
        self.token_url = token_url
        self.credentials = credentials
        self.refresh_token = refresh_token
        self.access_token = None
        self.token_expiration = None

    def get_token(self):
        '''If the token is expired retrieves a new one and stores it for next request. Otherwise returns stored one.'''

        if self.access_token and self.token_expiration and self.token_expiration > datetime.now():
            return self.access_token

        headers = {'Content-Type': 'application/json'}
        credentials_payload = json.dumps(self.credentials)
        response = requests.post(self.token_url, headers=headers, data=credentials_payload)
        if response.status_code == 200:
            token_info = response.json()
            self.access_token = token_info.get('access_token')
            expires_in = token_info.get('expires_in')
            self.token_expiration = datetime.now() + timedelta(seconds=expires_in)
            return self.access_token
        else:
            raise Exception("Failed to retrieve token")

    def is_token_valid(self):
        '''Quickly checks if is valid.'''
        
        if not self.access_token or not self.token_expiration:
            return False
        return self.token_expiration > datetime.now()
