# Marian

[![build-status](https://travis-ci.org/nebulousdog/marian.svg?branch=master)][travis-link]
[![coverage-status](https://coveralls.io/repos/github/nebulousdog/marian/badge.svg?branch=master)][coveralls-link]
[![package-status](https://img.shields.io/pypi/v/marian.svg)][pypi-link]

[travis-link]: https://travis-ci.com/nebulousdog/marian
[coveralls-link]: https://coveralls.io/github/nebulousdog/marian?branch=master
[pypi-link]: https://pypi.org/project/marian/

## Getting Started

Follow these instructions to get the Marian application going.

### Dependencies

```bash
git clone git@github.com:nebulousdog/marian.git
cd ./marian
# the install script includes `pipenv install --dev`
# likely need to make the install script executable with `chmod +x ./install.sh`
./install.sh
```

#### A few personal dev notes

All python dependencies are installed when you run `pipenv install`, but you're going to need `python3`, `pip3`, and [`pipenv`](https://github.com/pypa/pipenv) on your machine before you can get to that step. I'm not biased against Python2, but I'm going to be lazy about supporting it unless anyone asks for it.

This too is up to you. My personal setup has `python` and `pip` aliased to `python3` and `pip3` respectively. So, if you see this anywhere in the documentation know that I mean Python3.X.

```bash
alias python="python3"
alias pip="pip3"
```

Similarly, I use the [`./install.sh`](https://github.com/nebulousdog/marian/blob/master/install.sh) script for my development, but if you're not on a Debian-based machine you'll have to change the steps to get there.

Please feel free to [open an issue](https://github.com/nebulousdog/marian/issues) or [pull request](https://github.com/nebulousdog/marian/pulls) on getting this set up for any other environment!

### Run

There are two ways to get your username and password with Robinhood set up.

Firstly, you can simply start the application and any route will redirect you to the login page if a client has not been instantiated, and one is required. Flask by default runs on port 5000.

```bash
pipenv run flask run
firefox http://localhost:5000 # or http://localhost:5000/login
```

The second way is directly creating the `secrets.ini` file. There is an example one you can copy and edit the contents.

```bash
cp secrets_example.ini secrets.ini
```

After that, run `pipenv run flask run` and visit `https://localhost:5000`. See the Flask docs for [deployment options](http://flask.pocoo.org/docs/1.0/deploying/#deployment) and such.

#### Security Note

As you can see, **this will save your username and password in plain text.** This isn't the best, but doing so is slightly better than many Robinhood examples, where you're told to directly place your username and pass in the code. Such has the risk of you committing to the git history your personal info.

### Deploy

To deploy to Digital Ocean, you can use the deploy script.

```bash
python ./deploy.py
```

It is going to prompt you for an auth token. It will also be saved in the secrets file.

I'd love to hear if anyone uses this and does this differently, or has a secure suggestion.

## References

* https://github.com/westonplatter/fast_arrow
* https://github.com/pallets/flask
* https://api.robinhood.com/
* https://github.com/sanko/Robinhood

## Development

Include all development packages during installation with `pipenv install --dev`.

To activate this project's virtualenv, run `pipenv shell`. I start my text editor from inside the shell so that the Python related linting infos can be reported, such as not being able to import something. You can omit any of the prefixed `pipenv run <instruction>` pieces if you're already in the virtual environment shell.

### Tests

Simply run `pipenv run python -m pytest tests`.

### Linting

Simply run `pipenv run pylint **/*.py`.

## License

MIT
