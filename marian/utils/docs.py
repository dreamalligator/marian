import docutils.core

def generate_sphinx_docs():
    docutils.core.publish_file(
        source_path="README.rst",
        destination_path="./docs/index.html",
        writer_name="html"
    )
