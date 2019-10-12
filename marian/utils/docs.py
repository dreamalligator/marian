import docutils.core

def generate_full_docs():
    """use readme as landing page"""

    docutils.core.publish_file(
        source_path="./docs/index.rst",
        destination_path="./docs/index.html",
        writer_name="html",
    )

def generate_cli_help_doc():
    """runs ``marian`` once and copies that output to a docs/cli/help.txt doc."""

    from marian.cli import cli
    from click.testing import CliRunner

    cli_help_filename = './docs/cli/help.txt'
    with open(cli_help_filename, 'w') as doc_f:
        runner = CliRunner()
        result = runner.invoke(cli)
        doc_f.write(result.output)
