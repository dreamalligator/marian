'''
the Marian Flask application
'''

import urllib
import os
import inspect
from functools import wraps
import requests
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
from .utils.strings import hlt

def create_app(test_config=None):
    """
    basic factory.

    allows multiple instances of the application, with
    differing configs to be ran if need be.

    or could be used in tests, hint hint.
    """

    print('')
    print(hlt('Maid Marian started.'))
    print('https://github.com/nebulousdog/marian')
    print('')

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
        if request.method == 'POST':
            quiver.initialize_client(
                username=request.form['username'],
                password=request.form['password'],
            )

            if request.args.get('next') is None:
                return redirect(url_for('index'))

            return redirect(request.args.get('next'))

        return render_template('login.html')

    @app.route('/stylesheets/<path:path>')
    def send_stylesheet(path): # pylint: disable=unused-variable
        return send_from_directory('stylesheets', path)

    @app.route('/javascripts/<path:path>')
    def send_js(path): # pylint: disable=unused-variable
        return send_from_directory('javascripts', path)

    @app.route('/images/<path:path>')
    def send_img(path): # pylint: disable=unused-variable
        return send_from_directory('images', path)

    @app.route('/logout')
    def logout(): # pylint: disable=unused-variable
        session.clear()
        return redirect(url_for('index'))

    def login_required(self, f):
        """use saved session info to authenticate"""
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print('!!!', session.get('rh_username'), session)
            print('new methods at this point?', self)
            try:
                self.initialize_client(
                    username=session.get('rh_username'),
                    password=session.get('rh_password'),
                )
            except requests.exceptions.HTTPError:
                return redirect(url_for('login', next=request.url))

            return f(*args, **kwargs)

        return decorated_function

    @app.route('/test')
    @login_required
    def my_test_route(): # pylint: disable=unused-variable
        quiver.user.fetch() # pylint: disable=maybe-no-member

    return app
