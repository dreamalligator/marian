'''
simple robinhood utils that dont need anything instantiated with the Flask app,
nor the Fast Arrow client.
'''

def rh_id_from_instrument_url(url):
    """get the RH id from the instrument url. needed to look up stock data."""

    tokens = url.split("/")

    return tokens[4]
