from marian.utils.routes import route_info

def test_list_routes(app):
    info = route_info(app)
    assert list(info['headers']) == ['endpoint', 'methods', 'rule']
    assert str(info['routes'][0]['endpoint']) == 'index'
    assert info['routes'][0]['methods'] == 'GET,HEAD,OPTIONS'
