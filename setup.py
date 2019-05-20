import setuptools
from marian.version import __version__

with open('README.rst', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='marian',
    version=__version__,
    author='Tom Spalding',
    author_email='tom@catcobralizard.com',
    description='a personal Robinhood API server built on Fast Arrow.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    url='https://github.com/nebulousdog/marian',
    license='MIT',
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
