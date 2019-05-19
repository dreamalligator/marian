import datetime
from secrets import token_urlsafe
import jwt

def create_secret_key():
    """
    secret key for sessions.

    see http://flask.pocoo.org/docs/latest/config/#SECRET_KEY.
    """

    return token_urlsafe(64)

def encode_auth_token(app, user_id):
    '''
    create auth token for API authorization.

    spec claim name section: https://tools.ietf.org/html/rfc7519#section-4.1
    jwt encode api doc: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.encode
    '''

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id,
    }

    token = jwt.encode(
        payload,
        app.config.get('SECRET_KEY'),
        algorithm='HS256',
    )

    return token

def decode_auth_token(app, token):
    '''
    decode auth token.

    jwt decode api: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.decode
    '''

    decoded_token = jwt.decode(
        token,
        app.config.get('SECRET_KEY'),
        algorithms=['HS256'],
    )

    return decoded_token
