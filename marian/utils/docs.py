import docutils.core

def generate_sphinx_docs():
    """use readme as landing page"""

    docutils.core.publish_file(
        source_path="./docs/index.rst",
        destination_path="./docs/index.html",
        writer_name="html",
    )
