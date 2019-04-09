'''
simple utils used to read and write to config files.
'''

import configparser

SECRETS_FILENAME = 'secrets.ini'

def read_secrets(section, filename=SECRETS_FILENAME):
    """read in the secrets.ini file. return results from section."""

    secrets = configparser.ConfigParser()
    secrets.read(filename)

    return secrets[section]

def write_secrets(section, data):
    """write vars to section."""

    config = configparser.ConfigParser()
    config[section] = data

    with open(SECRETS_FILENAME, 'w') as secretfile:
        config.write(secretfile)
