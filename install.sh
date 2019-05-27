#!/usr/bin/env bash

echo 'install dependencies...'

# base system dependencies
sudo apt update
sudo apt install \
  git \
  python3 \
  python3-pip -y \
  ufw
sudo apt upgrade -y

pip3 install pipenv

# marian dependencies
cd marian || exit 1
pipenv install --dev

echo 'done.'
