"""deploy a fresh instance."""

import time
import paramiko.client
from marian.utils.deploy import (
    deploy_droplet,
    get_droplet,
    existing_droplets,
    retrieve_token,
)

if __name__ == '__main__':
    TOKEN = retrieve_token()
    EXISTING_DROPLETS = existing_droplets(TOKEN)
    print(f'{len(EXISTING_DROPLETS)} droplets already exist.')

    DEPLOY_RESPONSE = deploy_droplet(TOKEN)
    DROPLET_ID = DEPLOY_RESPONSE['id']

    while True:
        DROPLET_INFO = get_droplet(TOKEN, DROPLET_ID)

        if DROPLET_INFO['status'] == 'new':
            print('.')
            time.sleep(1)
            continue

        if DROPLET_INFO['status'] == 'active':
            DROPLET_IP = DROPLET_INFO['networks']['v4'][0]['ip_address']
            print(f'droplet is now active at {DROPLET_IP}.')

            CLIENT = paramiko.client.SSHClient()
            CLIENT.load_system_host_keys()
            # FIXME: paramiko.ssh_exception.SSHException: Server '159.89.130.229' not found in known_hosts
            CLIENT.connect(DROPLET_IP)

            CLIENT.exec_command('git clone https://github.com/nebulousdog/marian.git && cd marian')
            CLIENT.exec_command('sh ./install.sh')
            CLIENT.exec_command('sh ./serve.sh')

            break

        print('uguuuuu')
        raise NotImplementedError
