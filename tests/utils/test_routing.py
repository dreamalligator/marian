from flask import Flask

from marian.utils.routes import route_info

def get_app():
    """
    simple stub for route functions. could use memoized app fixture found in token tests, but
    dont need to see the full routes for this.
    """

    app = Flask(__name__)

    @app.route('/')
    def index(): # pylint: disable=unused-variable
        pass

    return app

def test_list_routes():
    info = route_info(get_app())
    assert list(info['headers']) == ['endpoint', 'methods', 'rule']
    assert str(info['routes'][0]['endpoint']) == 'index'
    assert info['routes'][0]['methods'] == 'GET,HEAD,OPTIONS'
