from marian.utils.deploy import (
    headers,
    retrieve_token,
)

def test_headers():
    assert headers('123')['Authorization'] == 'Bearer 123'

def test_retrieve_token():
    assert retrieve_token('DIGITALOCEAN_TOKEN_EXAMPLE') == 'k1ttyc4t'
