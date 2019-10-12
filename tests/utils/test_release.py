from marian.utils.release import (
    update_version,
)

def test_update_version(tmp_path):
    test_version_filepath = tmp_path / 'example_version_file.py'
    update_version(test_version_filepath, '13.13.13')

    read_file = open(test_version_filepath, 'r').read()
    assert read_file == '''"""!!!AUTOMATICALLY GENERATED!!! DO NOT EDIT.
see marian/release.py."""
__version__ = "13.13.13"
'''
