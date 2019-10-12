=========
👸 Marian
=========

.. image:: https://travis-ci.com/nebulousdog/marian.svg?branch=master
   :target: https://travis-ci.com/nebulousdog/marian
   :alt: travis-link
.. image:: https://codecov.io/gh/nebulousdog/marian/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/nebulousdog/marian
   :alt: codecov-link
.. image:: https://img.shields.io/pypi/v/marian.svg
   :target: https://pypi.org/project/marian/
   :alt: pypi-link

Find documentation at `nebulousdog.github.io/marian`_, and `github.com/nebulousdog/marian <https://github.com/nebulousdog/marian>`_.

.. _nebulousdog.github.io/marian: https://nebulousdog.github.io/marian

*******
Install
*******

Clone
=====

For devs this is the easiest.

.. code-block:: bash

  git clone --depth=1 git@github.com:nebulousdog/marian.git

PyPi
====

Marian is distributed via `PyPi <https://pypi.org/project/marian/>`_, and can be installed with ``pip install marian``.

***************
Running Locally
***************

.. code-block:: bash

  pip install pipenv
  pipenv install --dev
  pipenv run flask run

You'll now see the dynamically created routes.

.. image:: https://user-images.githubusercontent.com/2218331/60761769-c3fd9500-a004-11e9-9888-a3bbc9e8bb5f.png
   :alt: dynamically applied fast_arrow methods

This project is primarily a `Flask <https://github.com/pallets/flask>`_ app built on top of the `Fast Arrow`_ client. See `About This Project <https://github.com/nebulousdog/marian#about-this-project>`_ for more on that.

.. _Fast Arrow: https://github.com/westonplatter/fast_arrow/

You can now visit your locally running app at http://127.0.0.1:5000.

******
Deploy
******

simply run ``pipenv run python deploy``.

if this is your first time running this, you will be prompted for your Digital Ocean API token.

.. code-block:: bash

  > pipenv run python deploy.py
  Loading .env environment variables…
  Digital Ocean API token not found, retrieve your token from digitalocean.
  visit https://cloud.digitalocean.com/account/api/tokens.
  enter token:

Take note of the line that says ``droplet is now active at <ip address>``.

***********
Post Deploy
***********

TODO: working on that right now.

**************
Authentication
**************

Via Local Web App
=================

Visit the ``/login`` (http://localhost:5000/login) page to authenticate with Robinhood. Your client is subject to the same session durations that exist for the normal Robinhood app.

If you're navigating the app's frontend and you have no authenticated session yet, or need to re-authenticate, you will be automatically redirected to the login page as soon as you try to visit a route that requires authentication.

There are a few reasons that a frontend interface is provided:

* logging into Robinhood with a username/password allows a new user to immediately test Marian.
* this is the easiest UI way to create/regenerate auth tokens.
* all generated routes are supplied on the home page to immediately view what is available. these are clickable, which is nice for a new user.
* pleasant development environment.

That said though; **this mode is only available for local development.** My intent is to make things incredibly easy for new users or developers. However, after you're set up, auth tokens are meant to be the primary authentication method in production.

Via API
=======

Simply append your security token as a query param. For example, ``<marian path>?<query params>&token=<token>``.

To generate this token, run the app locally and visit http://localhost:5000/token. Here you can see your existing token, or generate a new one.

All old tokens will be invalidated after a token is regenerated.

***
API
***

Routes
======

You can find all supported routes by visiting the base route http://localhost:5000 locally.

Format
======

By default the output format is JSON. To output in a format that is more readily accepted by Google Sheets, you can supply a CSV param. For example, ``<marian path>?<query params>&csv``. Notice that the CSV param simply must exist. You may also write ``csv=true`` if you wish, but this is redundant.

Working with Google Sheets
==========================

You'll need two things from the deploy; the secure token generated, and the IP address of the droplet.

You can now import data into your sheet.

Example formula: ``=IMPORTDATA("<droplet ip>/stock_position/all&token=<token>")``

***
CLI
***

A CLI wrapper is provided with some handy functionality. This makes things easy for all, because only devs are going to want to use the Pipenv setup. Devs can also utilize the cli though! See the extended notes at `nebulousdog.github.io/marian`_.

See the available Marian cli commands with ``marian --help``.

******************
About This Project
******************

When writing Marian, my goal was just to get my `Robinhood <https://robinhood.com/>`_ data into a `Google Sheet <https://sheets.google.com>`_. If you've used Google Sheets at all, this is a PITA. Now it isn't.

There are some additional features that I added for my own learning and convenience that I'm proud to share:

* no plaintext saving of Robinhood usernames and passwords
* dynamically built routes. anything that `Fast Arrow`_ supports is automatically supported by Marian.
* deploy scripts
* API token generation
* CI and tests
* secure sessions and authentication
* frontend interface for developing
* headless production mode
* JSON and CSV API formats

Upcoming
========

The full list is located at https://github.com/nebulousdog/marian/issues.

*************
Configuration
*************

Since Marian is a Flask app, all Flask documentation applies for custom configuration. See http://flask.pocoo.org/docs/latest.

*****
Tests
*****

1. ``pipenv run tests``

*******
Linting
*******

1. ``pipenv run lints``

*********
Releasing
*********

1. ``pipenv run bump_version``

*******
License
*******

MIT
