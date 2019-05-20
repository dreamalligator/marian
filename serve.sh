#!/usr/bin/env bash

gunicorn "marian.app:create_app()"
