#!/usr/bin/env bash

cd marian || exit 1
gunicorn "marian.app:create_app()"
