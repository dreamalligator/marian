from marian.utils.deploy import (
    deploy_droplet,
    get_droplet_id,
    get_droplet_ip,
    get_key_fingerprints,
    get_key_ids,
    headers,
    refresh_droplet_cache,
    retrieve_token,
)

# def test_deploy_droplet():
#     pass("status code == not accepted")
#     pass("status code == ok")

def test_get_droplet_id():
    assert get_droplet_id() == '1312'

def test_get_droplet_ip():
    assert get_droplet_ip() == '6.6.6'

def test_get_key_fingerprints():
    assert get_key_fingerprints('birdperson') == 'k1ttyc1ty'

def test_get_key_ids():
    assert get_key_ids('birdperson') == ['123', '456']

def test_headers():
    assert headers('123')['Authorization'] == 'Bearer 123'

# def test_refresh_droplet_cache():
#     pass

# def test_retrieve_token():
#     pass
