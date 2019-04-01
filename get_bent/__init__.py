"""Flask Application"""

import os

from flask import Flask, jsonify, render_template

def create_app(test_config=None):
    """create app"""

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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
    def index():
        html = 'Find documentation at <a href="https://github.com/nebulousdog/lazy-money-maker">'
        html += 'https://github.com/nebulousdog/lazy-money-maker</a>.<br><br><hr><h2>Routes</h2>'
        html += list_routes()
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
            line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
            output.append(line)

        final_output = ''
        for line in sorted(output):
            final_output += line + '<br>'
        return final_output

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)

    @app.route('/positions')
    def positions():
        return jsonify([0, 0, 0])

    @app.route('/positions/<ticker>')
    def position(ticker):
        return f'found {ticker}'



    return app
