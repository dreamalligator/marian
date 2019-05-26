"""
WARNING: this takes down any droplets it finds.
"""

from marian.utils.deploy import (
    destroy,
    retrieve_token,
)

if __name__ == '__main__':
    destroy(retrieve_token())
