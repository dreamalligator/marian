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
