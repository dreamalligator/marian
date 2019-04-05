"""rh api related methods"""

import os.path
import json
from getpass import getpass
from flask import jsonify
from get_bent.secrets import username, password
import robin_stocks as r

def rh_login():
    """login using username and password to get token"""

    login_info = r.login(username, password)

    return jsonify(login_info)

def rh_holdings():
    """my portfolio positions"""

    r.login(username, password)

    my_stocks = r.build_holdings()

    return jsonify(my_stocks)
