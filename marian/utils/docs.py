import docutils.core

def generate_full_docs():
    """use readme as landing page"""

    docutils.core.publish_file(
        source_path="./docs/index.rst",
        destination_path="./docs/index.html",
        writer_name="html",
    )

def generate_cli_help_doc():
    """runs ``marian`` once and copies that output to a docs/cli/help.rst doc."""
