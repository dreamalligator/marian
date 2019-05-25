from marian.utils.deploy import (
    # deploy_droplet,
    # get_droplet_id,
    # get_droplet_ip,
    # get_key_fingerprints,
    # get_key_ids,
    headers,
    # refresh_droplet_cache,
    retrieve_token,
)

def test_deploy_droplet():
    pass

def test_get_droplet_id():
    pass

def test_get_droplet_ip():
    pass

def test_get_key_fingerprints():
    pass

def test_get_key_ids():
    pass

def test_headers():
    assert headers('123')['Authorization'] == 'Bearer 123'

def test_refresh_droplet_cache():
    pass

def test_retrieve_token():
    assert retrieve_token('DIGITALOCEAN_TOKEN_EXAMPLE') == 'k1ttyc4t'
