from requests import Session
from marian.utils.parse import boolean_query_param

def test_boolean_query_param(httpbin):
    session = Session()
    session.params['none_param'] = 'none'
    session.params['true_param'] = 'true'
    session.params['false_param'] = 'false'
    req = session.get(httpbin.url)
    assert boolean_query_param(req, 'none_param') is None
    assert boolean_query_param(req, 'true_param') is True
    assert boolean_query_param(req, 'false_param') is False
    assert boolean_query_param(req, 'none_param', None) is None
    assert boolean_query_param(req, 'none_param', True) is True
    assert boolean_query_param(req, 'none_param', False) is False
