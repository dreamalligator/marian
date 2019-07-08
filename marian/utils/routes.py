'''
some helpers for the templates.
'''

from functools import wraps

def route_info(app):
    """list the implemented Flask app's API routes."""

    output = {
        'headers': [],
        'routes': [],
    }

    i = 0

    for rule in app.url_map.iter_rules():
        info = {
            'endpoint': rule.endpoint,
            'methods': ','.join(sorted(rule.methods)),
            'rule': rule,
            # 'options': ','.join(sorted(rule.arguments)),
            # 'defaults': rule.defaults,
            # 'redirect_to': rule.redirect_to,
        }

        if i == 0:
            output['headers'] = info.keys()

        output['routes'].append(info)

        i += 1

    output['routes'].sort(key=lambda route: str(route['rule']))

    return output

def env_restricted(app, env=None):
    """restrict a route to a specific environment."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if env is None:
                raise ValueError('env must be supplied')

            if app.config.get('ENV') != env:
                return 'this route is restricted.'

            return f(*args, **kwargs)

        return decorated_function

    return decorator
