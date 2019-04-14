from marian.utils.config import read_secrets

def test_read_secrets():
    rh_secrets = read_secrets('rh_account', filename='secrets_example.ini')
    assert(rh_secrets == {'username': 'ricknmorty', 'password': 'gaggablaghblagh'})
