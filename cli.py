"""
CLI related utils.
"""

import click
from marian.version import __version__

# ``marian --help``: help
# ``marian --version``: version
# ``marian routes``: view all routes, including custom routes. this depends on whether Marian is running in development or production mode.
# ``marian routes --custom``: view just custom routes.
# ``marian routes --development``: view all development mode routes.
# ``marian routes --production``: view all production mode routes.
# ``marian token``: view current token
# ``marian token --regenerate``: regen token
# ``marian deploy``: deploy a Marian droplet
# ``marian deploy --status``: check if Marian has already deployed droplets. print their infos if so.
# ``marian destroy``: destroy all Marian droplets
# ``marian serve``: run Marian app.
# ``marian serve --development``: this is the default. run Marian in dev mode.
# ``marian serve --development --headless``: run headless but with dev config. production by default runs with --headless as true.
# ``marian serve --production``: run Marian with production config.
# ``marian query <route>``: may query any Marian endpoint. see ``Marian routes`` for full list.
# ``marian query <route> --csv``: output query in CSV format.
# ``marian query <route> --json``: output query in JSON format. this is default.

@click.group(invoke_without_command=True)
@click.version_option(version=__version__)
def cli():
    """
    Marian CLI
    https://nebulousdog.github.io/marian
    https://github.com/nebulousdog/marian
    """

@cli.command()
@click.option(
    '--custom',
    'route_switch',
    flag_value='custom',
    help='view just custom routes.',
)
@click.option(
    '--development',
    'route_switch',
    flag_value='development',
    help='view all routes for the development mode.',
)
@click.option(
    '--production',
    'route_switch',
    flag_value='production',
    help='view all routes for the production mode.',
)
def routes(route_switch):
    click.echo('routes go here')

    click.echo(route_switch)

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
@click.option(
    '--development'
)
@click.option(
    '--production'
)
def serve():
    click.echo('serve go here')

if __name__ == '__main__':
    cli()
