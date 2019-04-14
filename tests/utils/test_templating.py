from flask import Flask

from marian.utils.routes import list_routes

def get_app():
    """simple Flask app stub"""

    app = Flask(__name__)

    @app.route('/')
    def index(): # pylint: disable=unused-variable
        pass

    return app

def test_list_routes():
    generated_routes = list_routes(get_app())
    print('generated_routes', generated_routes)
    assert generated_routes[0] == 'index           GET,HEAD,OPTIONS          /'
