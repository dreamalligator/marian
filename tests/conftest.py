import pytest
import flask

@pytest.fixture
def app():
    test_app = flask.Flask(__name__)
    test_app.secret_key = 'sh3rw00d'

    @test_app.route('/')
    def index(): # pylint: disable=unused-variable
        pass

    return test_app

@pytest.fixture
def bash_0():
    return open('./tests/fixtures/bash_0.sh', 'r').read()

@pytest.fixture
def bash_1():
    return open('./tests/fixtures/bash_1.sh', 'r').read()

@pytest.fixture
def joined_script():
    return open('./tests/fixtures/joined_script.sh', 'r').read()
