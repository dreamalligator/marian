'''
the Lazy Money Maker Flask application
'''

import os

from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from .rudygood import RuddyGood
from .utils.templating import route_table
from .utils.config import write_secrets

def create_app(test_config=None):
    """
    basic factory.

    allows multiple instances of the application, with
    differing configs to be ran if need be.

    or could be used in tests, hint hint.
    """

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'lazy_money_maker.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # jinja templates
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # rude boy
    rudy = RuddyGood()

    @app.route('/')
    def index(): # pylint: disable=unused-variable
        return render_template('index.html', route_table=route_table(app))

    @app.route('/login', methods=['GET', 'POST'])
    def login(): # pylint: disable=unused-variable
        error = None

        if request.method == 'POST':
            write_secrets('rh_account', {
                'username': request.form['username'],
                'password': request.form['password'],
            })

            if request.args.get('next') is None:
                return redirect(url_for('index'))

            return redirect(request.args.get('next'))

        return render_template('login.html', error=error)

    # NOTE: csv=false evaluates to truthy, only care about existence of `csv`
    #   param atm, but really should clear that up.
    #   expecting only `/positions?csv` or `/positions`.
    @app.route('/positions')
    @rudy.login_required
    def positions(): # pylint: disable=unused-variable
        csv = request.args.get('csv') is not None
        return rudy.rh_positions(csv)

    @app.route('/collection/<tag>')
    @rudy.login_required
    def collection(tag): # pylint: disable=unused-variable
        return rudy.raw_collection(tag)

    @app.route('/quote/<symbol>')
    @rudy.login_required
    def quote(symbol): # pylint: disable=unused-variable
        return rudy.rh_quote(symbol)

    @app.route('/watchlist')
    @rudy.login_required
    def watchlist(): # pylint: disable=unused-variable
        return rudy.rh_watchlist()

    @app.route('/dividends')
    @rudy.login_required
    def dividends(): # pylint: disable=unused-variable
        return rudy.rh_dividends()

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
