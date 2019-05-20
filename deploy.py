"""deploy a fresh instance."""

from marian.utils.deploy import (
    deploy_droplet,
    retrieve_token,
)

if __name__ == '__main__':
    deploy_droplet(retrieve_token())
