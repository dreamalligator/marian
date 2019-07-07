Get both Pipenv and CLI
=======================

.. image:: https://user-images.githubusercontent.com/2218331/60773052-18ac1900-a0b4-11e9-8378-0402499aee3d.jpg
   :alt: why not both

The recommended installation is via cloning the repo, but this has the downside of requiring all cli commands to be run like ``pipenv run python cli.py --version``. before you go "wth!", let me tell you we got you covered! :D

simply run ``pipenv install -e``. now you have access to the full ``marian`` cli. it will also reflect your changes without having to install repeatedly after code changes.

test with ``marian --version``. hooray.

you can test that it is editable for example by modifying ``cli.py``'s group docstring (in ``def cli``). Then run ``marian`` by itself and you'll see your changes reflected for the default command.
