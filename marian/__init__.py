'''
the Marian Flask application
'''

import urllib
import os

from flask import (
    Flask,
    send_from_directory,
    render_template,
    redirect,
    request,
    session,
    url_for,
)

from .fast_arrow_quiver import FastArrowQuiver
from .utils.routes import route_info
from .utils.parse import boolean_query_param
from .utils.tokens import create_secret_key

def create_app(test_config=None):
    """
    basic factory.

    allows multiple instances of the application, with
    differing configs to be ran if need be.

    or could be used in tests, hint hint.
    """

    print('Maid Marian started.')

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    if app.config.get('SECRET_KEY') is None:
        app.config['SECRET_KEY'] = create_secret_key()

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    quiver = FastArrowQuiver()

    @app.route('/')
    def index(): # pylint: disable=unused-variable
        return render_template('index.html', route_info=route_info(app))

    @app.route('/login', methods=['GET', 'POST'])
    def login(): # pylint: disable=unused-variable
        error = None

        if request.method == 'POST':
            quiver.initialize_client(
                username=request.form['username'],
                password=request.form['password'],
            )

            if request.args.get('next') is None:
                return redirect(url_for('index'))

            return redirect(request.args.get('next'))

        return render_template('login.html', error=error)

    @app.route('/positions')
    @quiver.login_required
    def positions(): # pylint: disable=unused-variable
        csv = boolean_query_param(request, 'csv', True)
        return quiver.rh_positions(csv)

    @app.route('/collection/<tag>')
    @quiver.login_required
    def collection(tag): # pylint: disable=unused-variable
        return quiver.fa_collection(tag)

    @app.route('/quote/<symbol>')
    @quiver.login_required
    def quote(symbol): # pylint: disable=unused-variable
        return quiver.rh_quote(symbol)

    @app.route('/watchlist')
    @quiver.login_required
    def watchlist(): # pylint: disable=unused-variable
        return quiver.rh_watchlist()

    @app.route('/dividends')
    @quiver.login_required
    def dividends(): # pylint: disable=unused-variable
        return quiver.rh_dividends()

    @app.route('/stylesheets/<path:path>')
    def send_stylesheet(path): # pylint: disable=unused-variable
        return send_from_directory('stylesheets', path)

    @app.route('/javascripts/<path:path>')
    def send_js(path): # pylint: disable=unused-variable
        return send_from_directory('javascripts', path)

    @app.route('/images/<path:path>')
    def send_img(path): # pylint: disable=unused-variable
        return send_from_directory('images', path)

    return app
