"""
Marian command line utility.
"""

import click
from marian.version import __version__

@click.group()
@click.version_option(version=__version__)
def cli():
    """
    Marian CLI 👸

    https://nebulousdog.github.io/marian

    https://github.com/nebulousdog/marian
    """

@cli.command()
def routes():
    import os
    os.system('flask routes')

@cli.command()
def token():
    click.echo('token go here')

@cli.command()
def deploy():
    from deploy import main
    main()

@cli.command()
def destroy():
    from destroy import main
    main()

@cli.command()
@click.argument(
    'environment',
    envvar='FLASK_ENV',
)
def serve(environment):
    import os
    if environment == 'production':
        os.system('sh ./serve.sh')
    else:
        os.system('flask run')

@cli.command()
def docs():
    from docs import main
    main()
