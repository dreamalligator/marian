#!/usr/bin/env bash

sudo apt update
sudo apt install \
  git \
  python3 \
  python3-pip
sudo apt upgrade -y

git clone --depth=1 https://github.com/nebulousdog/marian.git
