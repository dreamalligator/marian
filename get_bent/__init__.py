"""Flask Application"""

import os

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_from_directory,
)
from get_bent.robinhood import (
    raw_collection,
    rh_dividends,
    rh_positions,
    rh_quote,
    rh_watchlist,
)

def create_app(test_config=None):
    """create app"""

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'get_bent.sqlite'),
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

    @app.route('/')
    def index(): # pylint: disable=W0612
        html = 'Find documentation at <a href="https://github.com/nebulousdog/lazy-money-maker">'
        html += 'https://github.com/nebulousdog/lazy-money-maker</a>.<br><br><hr><h2>Routes</h2>'
        html += '<pre>'
        html += list_routes()
        html += '</pre>'
        html += '<br><br><hr><br>🐈'
        return html

    def list_routes():
        import urllib
        output = []
        for rule in app.url_map.iter_rules():
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            line = urllib.parse.unquote("{:15s} {:20s} {}".format(rule.endpoint, methods, rule))
            output.append(line)

        final_output = ''
        for line in sorted(output):
            final_output += line + '<br>'
        return final_output

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None): # pylint: disable=W0612
        return render_template('hello.html', name=name)

    @app.route('/positions')
    def positions(): # pylint: disable=W0612
        csv = request.args.get('csv')
        return rh_positions(csv)

    @app.route('/collection/<tag>')
    def collection(tag): # pylint: disable=W0612
        return raw_collection(tag)

    @app.route('/quote/<symbol>')
    def quote(symbol): # pylint: disable=W0612
        return rh_quote(symbol)

    @app.route('/watchlist')
    def watchlist(): # pylint: disable=W0612
        return rh_watchlist()

    @app.route('/dividends')
    def dividends(): # pylint: disable=W0612
        return rh_dividends()

    @app.route('/login')
    def login(): # pylint: disable=W0612
        return '''
            <h1>log in</h1>
            <input type="text">
            <input type="password">
            '''

    @app.route('/stylesheets/<path:path>')
    def send_stylesheet(path): # pylint: disable=W0612
        return send_from_directory('stylesheets', path)

    @app.route('/javascripts/<path:path>')
    def send_js(path): # pylint: disable=W0612
        return send_from_directory('javascripts', path)

    return app
