import json
import os
import urllib.parse

import requests

AUTH_USERNAME = os.getenv('AUTH_USERNAME')
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')
AUTH_CLIENT_ID = os.getenv('AUTH_CLIENT_ID')
AUTH_LOGIN_URL = urllib.parse.urljoin(os.getenv('AUTH_URL'), 'v1/login')

AUTH_TOKENS_STORAGE = {
    'access_token': '',
    'refresh_token': ''
}


def _save_tokens(storage, tokens):
    tokens = json.loads(tokens.content.decode("utf-8"))['data']
    storage['access_token'] = tokens['access_token']
    storage['refresh_token'] = tokens['refresh_token']


def _refresh_tokens(login, password, client_id):
    auth_url = AUTH_LOGIN_URL
    auth_data = {
        'data': {
            'username': login,
            'password': password,
            'client_id': client_id
        }
    }
    return requests.post(auth_url, json=auth_data, verify=False)


def get_tokens(storage):
    return {
        'access': storage['access_token'],
        'refresh': storage['refresh_token']
    }


def token_updater(fn):
    def fn_wrapper(storage, *args, **kwargs):
        result = fn(storage, *args, **kwargs)
        if (result.status_code == 200):
            return result
        credentials = {
            'login': AUTH_USERNAME,
            'password': AUTH_PASSWORD,
            'client_id': AUTH_CLIENT_ID
        }
        _save_tokens(storage, _refresh_tokens(**credentials))
        return fn(storage, *args, **kwargs)

    return fn_wrapper
