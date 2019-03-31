# Lazy Money Maker

![build-status](https://travis-ci.org/nebulousdog/lazy-money-maker.svg?branch=master)

## Getting Started

Follow these instructions to get the Lazy Money Maker application going.

### Dependencies

All python dependencies are installed when you run `pipenv install`, but you're going to need `python3`, `pip3`, and `pipenv` on your machine before you can get to that step. I use the `./install.sh` script for my development, but if you're not in a Debian-based machine you'll have to change the steps to get there.

```bash
git clone git@github.com:nebulousdog/lazy-money-maker.git
cd ./lazy-money-maker
# the install script includes `pipenv install --dev`
# may need to make install script executable with `chmod +x ./install.sh`
./install.sh
```

Use `pipenv` for all dependencies.

## Development

> To activate this project's virtualenv, run `pipenv shell`.

## Tests

Simply run `pipenv run pytest`.

## Linting

Simply run `pipenv run pylint **/*.py`.

## License

MIT
