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
    """Show all routes based on FLASK_ENV configuration."""

    import os
    os.system('flask routes')

@cli.command()
def token():
    """
    Show secret api token.

    Do not share this with anyone.
    """

@cli.command()
def deploy():
    """Deploy to a Digital Ocean droplet."""

    from deploy import main
    main()

@cli.command()
def destroy():
    """Destroy all Marian Digital Ocean droplets."""
    from destroy import main
    main()

@cli.command()
@click.option(
    '--show',
    is_flag=True,
    default=False,
    help='optionally open generated file to view docs automatically.',
)
def docs(show):
    """Generate documentation."""

    from docs import main
    main()

    if show:
        click.launch('./docs/index.html')

@cli.command()
@click.argument(
    'environment',
    envvar='FLASK_ENV',
)
def serve(environment):
    """Run Marian application based on FLASK_ENV configuration."""

    import os
    if environment == 'production':
        os.system('sh ./serve.sh')
    else:
        os.system('flask run')
