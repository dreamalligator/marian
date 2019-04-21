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

Marian at her heart is an API server application for `Robinhood <https://robinhood.com>`_. The endpoints are dynamically built on `Fast Arrow <https://github.com/westonplatter/fast_arrow>`_. As such, it is easily extendable.

*************
Google Sheets
*************

My original goal was to make importing data into `Google Sheets <https://developers.google.com/apps-script/guides/sheets>`_ easier. The pain points are quickly realized. Here are some nice features this project has that will make your life easier with Sheets.

* secure and encrypted saving of login details.
* generate auth tokens for yourself.
* every Robinhood endpoint is supported that Fast Arrow supports.
* every endpoint returns data in CSV format simply by adding a ``csv`` param.
* work in your own dev environment with all perks of such.

********
Features
********

My favorite part of the project is that each base endpoint is dynamically created. Supported endpoints will automatically be added as they are added to Fast Arrow. Each of these endpoints is additionally decorated to require authorized logins, export in CSV format, and attaches the requisite Fast Arrow client that persists your connection. This simplifies the number of params to pass along. Routes for every one of these methods is created as well.

.. image:: https://user-images.githubusercontent.com/2218331/56465106-379be880-63ac-11e9-8ac0-574911f7fa2f.png
   :alt: dynamically applied fast_arrow methods

The other features are basically just features of being a Flask application, but here are some other highlights:

* add your own endpoints and routes with no hassle.
* deploy to Digital Ocean
* security in mind during every step

***************
Getting Started
***************

Follow these instructions to get the Marian application going.

Install
=======

Need :code:`python3`, :code:`pip3`, and :code:`pipenv` installed first. Then run :code:`pipenv install`.

Run
===

To get your username and password with Robinhood set up, start the application (:code:`pipenv run flask run`) and any route will redirect you to the login page (:code:`http://localhost:5000/login`) if a client has not been instantiated, and one is required.

For running in production environment, use ``pipenv run serve`` or :code:`pipenv run sh ./serve.sh`. This uses ``gunicorn`` which is better for production environment.

Deploy
======

To deploy to Digital Ocean, you can use the deploy script.

Equivalent:
* ``pipenv run deploy``
* ``pipenv run python ./deploy.py``

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

Run ``pipenv run tests`` or ``pipenv run python -m pytest --cov=marian tests``.

Linting
=======

Run ``pipenv run lint`` or ``pipenv run pylint **/*.py``.

Documentation
=============

* Sphinx docs: `nebulousdog.github.io/marian/ <https://nebulousdog.github.io/marian/>`_
* Github: `github.com/nebulousdog/marian <https://github.com/nebulousdog/marian>`_
* Generate: ``pipenv run docs`` or ``pipenv run sphinx-build -b html docs/src docs/html``

*******
License
*******

MIT
