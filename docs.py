from marian.utils.docs import (
    generate_cli_help_doc,
    generate_full_docs,
)

if __name__ == "__main__":
    print('running marian cli once for output')
    generate_cli_help_doc()
    print('generated at docs/cli.rst')

    print('generating docs...')
    generate_full_docs()
    print('done with docs.')
