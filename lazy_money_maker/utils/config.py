'''
simple utils used to read and write to config files.
'''

import os.path
import configparser

SECRETS_FILENAME = 'secrets.ini'

def read_secrets(section, filename=SECRETS_FILENAME):
    """read in the secrets.ini file. return results from section."""

    secrets = configparser.ConfigParser()
    if os.path.isfile(filename):
        secrets.read(filename)
    else:
        raise FileNotFoundError(f'Can\'t read non-existent file, {filename}.')

    return secrets[section]

def write_secrets(section, data, filename=SECRETS_FILENAME):
    """write vars to section."""

    config = configparser.ConfigParser()
    config[section] = data

    with open(filename, 'w') as secret_f:
        config.write(secret_f)
        secret_f.close()
