import string
from marian.utils.tokens import (
    create_secret_key,
    decode_auth_token,
    encode_auth_token,
)

def test_create_secret_key():
    """
    nothing special about create_secret_key atm. this redundantly tests that
    token_urlsafe does what it says.
    https://github.com/python/cpython/blob/3.7/Lib/test/test_secrets.py#L113
    """

    secret = create_secret_key()
    assert isinstance(secret, str)
    legal_chars = string.ascii_letters + string.digits + '-_'
    assert all(c in legal_chars for c in secret)

def test_encode_auth_token(app): # pylint: disable=redefined-outer-name
    auth_token = encode_auth_token(app, 's1r_h1ss')
    assert isinstance(auth_token, bytes)

def test_decode_auth_token(app): # pylint: disable=redefined-outer-name
    token = encode_auth_token(app, 'm41d_m4r14n')
    assert decode_auth_token(app, token)['sub'] == 'm41d_m4r14n'
