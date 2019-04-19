######
Marian
######

.. image:: https://travis-ci.org/nebulousdog/marian.svg?branch=master
   :target: https://travis-ci.com/nebulousdog/marian
   :alt: travis-link
.. image:: https://coveralls.io/repos/github/nebulousdog/marian/badge.svg?branch=master
   :target: https://coveralls.io/github/nebulousdog/marian?branch=master
   :alt: coveralls-link
.. image:: https://img.shields.io/pypi/v/marian.svg
   :target: https://pypi.org/project/marian/
   :alt: pypi-link

* no setup other than cloning project or installing as a dependency. just log in, and if you hit an endpoint requiring authentication, you will be redirected to the login page, and navigated back to where you were after.
* deploy to Digital Ocean easily. the deploy script will walk you through it. or, you can automatically deploy with Travis-CI during development.
* secure authentication. no saving plain text files like many of the peer Robinhood code projects.
* all the regular benefits of being a Flask application. for example, can extend the base routes as you wish, or run multiple instances of the app easily.
* every endpoint can parse in CSV format. this makes importing in Google Sheets very easy. You'll like this if you have ever written shitty Google apps scripts for your sheets.
* create auth tokens for yourself. this will allow google sheets to access the api while keeping your sensitive data private.

***************
Getting Started
***************

Follow these instructions to get the Marian application going.

Install
=======

Need :code:`python3`, :code:`pip3`, and :code:`pipenv` installed first. Then run :code:`pipenv install --dev`.

Run
===

To get your username and password with Robinhood set up, start the application (:code:`pipenv run flask run`) and any route will redirect you to the login page (:code:`http://localhost:5000/login`) if a client has not been instantiated, and one is required.

Deploy
======

To deploy to Digital Ocean, you can use the deploy script.

.. code:: bash

  python ./deploy.py

**********
References
**********

* https://github.com/westonplatter/fast_arrow
* https://github.com/pallets/flask
* https://api.robinhood.com/
* https://github.com/sanko/Robinhood

***********
Development
***********

Include all development packages during installation with :code:`pipenv install --dev`.

To activate this project's virtualenv, run :code:`pipenv shell`. I start my text editor from inside the shell so that the Python related linting infos can be reported, such as not being able to import something. You can omit any of the prefixed :code:`pipenv run <instruction>` pieces if you're already in the virtual environment shell.

Tests
=====

Run :code:`pipenv run python -m pytest --cov=marian tests`.

Linting
=======

Run :code:`pipenv run pylint **/*.py`.

*******
License
*******

MIT
