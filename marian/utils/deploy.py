"""digital ocean deploy utils"""

import os.path
# if I understand correctly, both standard json and simplejson are the same,
# except that standard json is based on an older simplejson version and lagging,
# while simplejson will be kept up to date with Flask.
from flask import json
import requests

def deploy_droplet(token):
    """deploy a new droplet."""

    droplet_info = {
        'name': 'marian',
        'region': 'sfo2',
        'size': '4gb',
        'image': 'ghost-18-04',
        'ssh_keys': get_key_fingerprints(token)
    }

    print('deploying new droplet...')
    url = 'https://api.digitalocean.com/v2/droplets'
    request = requests.post(url, headers=headers(token), params=droplet_info)

    # see https://github.com/requests/requests/blob/master/requests/status_codes.py
    # pylint: disable=E1101
    if request.status_code != requests.codes.accepted:
        print('Something went wrong. ' + request.json()['message'])
        return

    print('Deployed! 👸')

def get_droplet_id():
    """get droplet id from cached info, prevents unnecessary requests."""

    cached_droplet_info_file = 'droplet_info.json'

    with open(cached_droplet_info_file, 'r') as info_f:
        droplet_info = json.load(info_f)
        return droplet_info['id']

def get_droplet_ip():
    """get droplet ip from cache."""

    cached_droplet_info_file = 'droplet_info.json'

    with open(cached_droplet_info_file, 'r') as info_f:
        droplet_info = json.load(info_f)
        return droplet_info['networks']['v4'][0]['ip_address']

def get_key_fingerprints(token):
    """
    Using ssh_key fingerprints because array of ids seems broken on Digital
    Ocean's side.
    """

    request = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers(token))

    return list(map(lambda key: key['fingerprint'], request.json()['ssh_keys']))

def get_key_ids(token):
    """get a key to embed when making a new droplet."""

    request = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers(token))

    return list(map(lambda key: key['id'], request.json()['ssh_keys']))

def headers(token):
    """heads up."""

    headers_obj = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    return headers_obj

def refresh_droplet_cache(token):
    """
    check if have saved catcobralizard droplet info, or retrieve it.
    see https://cloud.digitalocean.com/account/api/tokens.
    """

    cached_droplet_info_file = 'droplet_info.json'

    print('attempting to retrieve catcobralizard info...')

    request = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers(token))

    refreshed = False
    for droplet in request.json()['droplets']:
        if droplet['name'] == 'catcobralizard':
            with open(cached_droplet_info_file, 'w') as info_f:
                info_f.write(json.dumps(droplet))
            droplet_id = droplet['id']
            print(f'saving info for droplet {droplet_id}...')
            refreshed = True
            break

    if not refreshed:
        print('no catcobralizard droplets found.')

def retrieve_token():
    """
    check if have a saved Digital Ocean API token, or retreive one.
    """

    token_file_name = 'DIGITALOCEAN_TOKEN'

    if os.path.isfile(token_file_name):
        print('token found...')

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
