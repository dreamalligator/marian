"""query parsing utils"""

def boolean_query_param(request, param_name, convert_none=None):
    '''
    convert query params to boolean.

    if optional convert_none value is passed along, None values will be
    converted to such.
    '''

    raw_param = request.args.get(param_name)
    if raw_param == 'none':
        if convert_none is None:
            return None
        return convert_none

    str_param = raw_param.lower()
    if str_param == 'true':
        return True

    return False
