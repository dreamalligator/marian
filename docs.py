#!/usr/bin/env python

"""
A script to generate all docs.
"""

from marian.utils.docs import (
    generate_cli_help_doc,
    generate_full_docs,
)

def main():
    print('running marian cli once for output')
    generate_cli_help_doc()
    print('generated at docs/cli.rst')

    print('generating docs...')
    generate_full_docs()
    print('done with docs.')

if __name__ == "__main__":
    main()
