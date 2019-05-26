"""
WARNING: this takes down any droplets it finds.
"""

from marian.utils.deploy import destroy

if __name__ == '__main__':
    destroy()
