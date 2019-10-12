"""deploy a fresh instance."""

import time
from marian.utils.deploy import (
    deploy_droplet,
    get_droplet,
    existing_droplets,
    retrieve_token,
)

def main():
    token = retrieve_token()
    existing = existing_droplets(token)
    print(f'{len(existing)} droplets already exist.')

    deploy_response = deploy_droplet(token)
    droplet_id = deploy_response['id']

    while True:
        droplet_info = get_droplet(token, droplet_id)

        if droplet_info['status'] == 'new':
            print('.')
            time.sleep(1)
            continue

        if droplet_info['status'] == 'active':
            droplet_ip = droplet_info['networks']['v4'][0]['ip_address']
            print(f'droplet is now active at {droplet_ip}.')
            print(f'See https://github.com/nebulousdog/marian#marian.')

            print('TODO: use user_data script (already running remotely \
                hopefully) or ssh and run script here.')

            break

        print('uguuuuu')
        raise NotImplementedError

if __name__ == '__main__':
    main()
