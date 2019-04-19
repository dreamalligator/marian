import flask
from marian.utils.parse import boolean_query_param

def test_boolean_query_param(app):
    url = '/path?none_param=none&true_param=true&false_param=false'
    with app.test_request_context(url):
        assert boolean_query_param(flask.request, 'none_param') is None
        assert boolean_query_param(flask.request, 'true_param') is True
        assert boolean_query_param(flask.request, 'false_param') is False
        assert boolean_query_param(flask.request, 'none_param', None) is None
        assert boolean_query_param(flask.request, 'none_param', True) is True
        assert boolean_query_param(flask.request, 'none_param', False) is False
