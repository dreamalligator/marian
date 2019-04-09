from flask import Flask

from lazy_money_maker.utils.templating import list_routes

def get_app():
    """simple Flask app stub"""

    app = Flask(__name__)

    @app.route('/')
    def index(): # pylint: disable=unused-variable
        pass

    return app

def test_list_routes():
    assert list_routes(get_app())[0] == 'index           GET,HEAD,OPTIONS     /'
