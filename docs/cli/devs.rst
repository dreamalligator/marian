Get both Pipenv and CLI
=======================

.. image:: https://user-images.githubusercontent.com/2218331/60773052-18ac1900-a0b4-11e9-8378-0402499aee3d.jpg
   :alt: why not both

The recommended installation is via cloning the repo, but this has the downside of requiring all cli commands to be run like ``pipenv run python cli.py --version``. Before you go "wth!", let me tell you we got you covered! :D

Simply run ``pip install -e .``. Now you have access to the full ``marian`` cli. It will also reflect your changes without having to install repeatedly after code changes.

Test with ``marian --version``. Hooray!

You can test that it is editable for example by modifying a ``marian/cli.py`` function. Run that command and witness your changes reflected in the output.
