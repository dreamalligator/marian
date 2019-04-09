'''
some helpers for the templates.
'''

import urllib

def list_routes(app):
    """list the implemented Flask app's API routes."""

    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = f'[{arg}]'

        methods = ','.join(sorted(rule.methods))
        line = urllib.parse.unquote("{:15s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    return sorted(output)
