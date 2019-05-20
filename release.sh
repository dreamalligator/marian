#!/usr/bin/env bash

version_error() {
  echo "must supply version argument like \"0.0.10\"."
  echo "exiting..."
  exit 1
}

if [ $# -eq 0 ]
then version_error
fi

# has to be at least 5 chars long for valid semver (x.x.x) version.
len=${#1}
if [ $len -ge 5 ]
then
  echo "__version__ = \"$1\"" > ./marian/version.py
else version_error
fi

git add -A
git commit -m "release v$1"

git tag v$1
git push --tags
