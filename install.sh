#!/usr/bin/env bash

sudo apt-get install python3-pip
pip3 install --user pipenv
pipenv install --dev
touch get_bent/secrets.py
