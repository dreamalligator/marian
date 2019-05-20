import docutils.core

def generate_sphinx_docs():
    """use readme as landing page"""

    docutils.core.publish_file(
        source_path="README.rst",
        destination_path="./docs/index.html",
        writer_name="html"
    )
