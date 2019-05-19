'''
some helpers for the templates.
'''

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
