#!/usr/bin/env bash

touch test.txt
sudo apt update
sudo apt install \
  git \
  python3 \
  python3-pip
sudo apt upgrade -y

# TODO?
# git clone --depth=1 https://github.com/nebulousdog/marian.git
# pip3 install marian
