"""digital ocean deploy utils"""

import os.path
import requests
from marian.utils.scripts import (
    join_bash_scripts,
    open_files,
)

def deploy_droplet(token):
    """
    deploy a new droplet. return the droplet infos so that it can be used to
    further provision.
    """

    # after deploying, run the following scripts to install, then serve app
    # via wsgi
    scripts = open_files(['./install.sh', './serve.sh'])

    droplet_info = {
        'name': 'marian',
        'region': 'sfo2',
        'size': '4gb',
        'image': 'ubuntu-18-04-x64',
        'ssh_keys[]': get_key_fingerprints(token),
        'user_data': join_bash_scripts(scripts),
    }

    print('deploying new droplet...')
    url = 'https://api.digitalocean.com/v2/droplets'
    request = requests.post(url, headers=headers(token), params=droplet_info)

    # see https://github.com/requests/requests/blob/master/requests/status_codes.py
    # pylint: disable=E1101
    if request.status_code != requests.codes.accepted:
        print('Something went wrong. ' + request.json()['message'])
        request.raise_for_status()

    droplet_infos = request.json()['droplet']
    droplet_id = droplet_infos['id']
    print(f'Deployed Marian 👸 (id: {droplet_id})!')
    return droplet_infos

def destroy():
    """
    take down the droplet by name.

    this is useful when testing deploying to keep taking down all the droplets
    of the name "marian".
    """

    print('destroy is a noop atm')

def get_key_fingerprints(token):
    """fingerprints of keys authorized with DO to embed when making a new droplet."""

    request = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers(token))

    return list(map(lambda key: key['fingerprint'], request.json()['ssh_keys']))

def get_key_ids(token):
    """ids of keys authorized with DO to embed when making a new droplet."""

    request = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers(token))

    return list(map(lambda key: key['id'], request.json()['ssh_keys']))

def get_pub_key():
    """could use some feedback on security."""

    return input("enter pub key:")

def add_pub_key(token):
    """upload public key to DO account."""

    params = {
        'name': 'basic',
        'public_key': get_pub_key(),
    }

    request = requests.post(
        'https://api.digitalocean.com/v2/account/keys',
        headers=headers(token),
        params=params,
    )

    # see https://github.com/requests/requests/blob/master/requests/status_codes.py
    # pylint: disable=E1101
    if request.status_code == requests.codes.created:
        print('done.')
        return

    print(request.json()['message'])

def headers(token):
    """heads up."""

    headers_obj = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    return headers_obj

def retrieve_token(token_file_name='DIGITALOCEAN_TOKEN'):
    """
    check if have a saved Digital Ocean API token, or retreive one.
    """

    if os.path.isfile(token_file_name):
        print('token found.')

        with open(token_file_name, 'r') as token_f:
            digitalocean_token = token_f.read().replace('\n', '')
    else:
        digitalocean_token = input(
            '''Digital Ocean API token not found, retrieve your token from digitalocean.
visit https://cloud.digitalocean.com/account/api/tokens.
enter token: '''
        )

        with open(token_file_name, 'w') as token_f:
            token_f.write(digitalocean_token)

        print('token saved to DIGITALOCEAN_TOKEN.')

    return digitalocean_token
