"""rh api related methods"""

import os.path
import json
from getpass import getpass
from flask import jsonify
import robin_stocks as r

def retrieve_token():
    """retrieve token. if not found, login and retrieve."""

    token_file_name = 'rh_login_info.json'

    if os.path.isfile(token_file_name):
        print('token found...')

        with open(token_file_name, 'r') as token_f:
            login_json = token_f.read()

    else:
        login_json = rh_login()

        with open(token_file_name, 'w') as token_f:
            login_text = json.dumps(login_json)
            token_f.write(login_text)

        print(f'token saved to {token_file_name}.')

    return login_json

def get_username():
    """get RH username"""
    return input('Enter your username: ')

def get_password():
    """get RH password"""
    return getpass('Enter your password: ')

def rh_login(username=get_username(), password=get_password()):
    """login using username and password to get token"""

    login_info = r.login(username, password)

    return jsonify(login_info)

def rh_holdings():
    """my portfolio positions"""

    my_stocks = r.build_holdings()

    output = []
    for key, value in my_stocks.items():
        output.append(f'{key}: {value}')

    return ''.join(output)
