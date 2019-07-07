"""deploy a fresh instance."""

import time
from marian.utils.deploy import (
    deploy_droplet,
    get_droplet,
    existing_droplets,
    retrieve_token,
)

def main():
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
            print(f'See https://github.com/nebulousdog/marian#marian.')

            print('TODO: use user_data script (already running remotely \
                hopefully) or ssh and run script here.')

            break

        print('uguuuuu')
        raise NotImplementedError

if __name__ == '__main__':
    main()
