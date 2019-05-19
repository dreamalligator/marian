#!/usr/bin/env bash

gunicorn "marian:create_app()"
