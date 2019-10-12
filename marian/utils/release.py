"""utils for the release process."""

import sys
import subprocess
from marian.version import __version__

def run(cmd):
    return subprocess.getoutput(cmd)

def update_version(version_file_path, version_str):
    """update the version file."""

    prefixed_warning = """\"\"\"!!!AUTOMATICALLY GENERATED!!! DO NOT EDIT.
see marian/release.py.\"\"\"\n"""

    version_doc = f'{prefixed_warning}__version__ = "{version_str}"\n'

    with open(version_file_path, 'w') as f:
        f.write(version_doc)
        f.close()

def version_error():
    """print that invalid semver was supplied and exit with error code 1."""

    print('must supply version argument like "0.0.10".')
    print('exiting...')
    sys.exit(1)

def update_version_and_tag_for_release():
    """
    full process. utilized by root release script.

    if master branch:
        1. bump version
        2. commit
        3. tag
        4. push both

    otherwise, just commit the bumped version.
    """

    print(f'current version is {__version__}.')

    if len(sys.argv) > 1:
        new_version = sys.argv[1]
    else:
        try:
            new_version = input(
                '''what do you want the new version to be?
enter new version: '''
            )
        except (KeyboardInterrupt, EOFError):
            print('\nexiting...')
            sys.exit(0)

    if new_version == '' or new_version.count('.') != 2 or len(new_version) < 5:
        version_error()

    update_version(f'marian/version.py', new_version)

    print(f'version updated to {new_version}.')

    run('git add -A')
    run(f'git commit -m "release v{new_version}"')

    current_branch = run('git symbolic-ref --short HEAD')
    print(f'\nOn {current_branch} branch...')
    if current_branch == 'master':
        # must use annotated tags if using --follow-tags
        run(f'git tag -a {new_version} -m "v{new_version}"')
        run('git push --follow-tags')
        print('tags and commits pushed.\n')
        print(f'''after CI runs at https://travis-ci.org/nebulousdog/marian,
find new releases at all the following locations:
* Github Releases: https://github.com/nebulousdog/marian/releases
* PyPI: https://pypi.org/project/marian/
* Github Pages: https://nebulousdog.github.io/marian/
''')
    else:
        print('Quick releases are only performed on the master branch.')
