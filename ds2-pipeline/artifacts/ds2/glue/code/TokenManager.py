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
    '''Class for managing access tokens.'''

    def __init__(self, token_url, credentials, refresh_token):
        '''Initialize TokenManager with token URL, credentials, and refresh token.'''
        self.token_url = token_url
        self.credentials = credentials
        self.refresh_token = refresh_token
        self.access_token = None
        self.token_expiration = None

    def get_token(self):
        '''Retrieve a new token if expired or return the stored one.'''
        
        if self.access_token and self.token_expiration and self.token_expiration > datetime.now():
            return self.access_token

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.token_url, headers=headers, data=self.credentials)
        response.raise_for_status()  # Raise an exception for bad status codes
        token_info = response.json()
        self.access_token = token_info.get('access_token')
        expires_in = token_info.get('expires_in')
        self.token_expiration = datetime.now() + timedelta(seconds=expires_in)
        return self.access_token

    def is_token_valid(self):
        '''Check if the token is valid.'''
        
        return self.access_token and self.token_expiration and self.token_expiration > datetime.now()