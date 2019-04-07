"""rh api related methods."""

from flask import jsonify
from fast_arrow import (
    Client,
    Collection,
    Dividend,
    Stock,
    StockMarketdata,
    StockPosition,
)
from get_bent.secrets import username, password

CLIENT = None

def rh_client():
    """start and memoize a RH connection via fast_arrow."""

    global CLIENT # pylint: disable=W0603

    if CLIENT is None:
        print(f'authenticating for {username}...')
        CLIENT = Client(username=username, password=password)
        CLIENT.authenticate()
        print('done.')

    return CLIENT

def raw_dividends():
    """raw dividends via fast_arrow"""

    return Dividend.all(rh_client())

def rh_dividends():
    """rh dividend infos formatted for personal use"""

    dividends = raw_dividends()

    return jsonify(dividends)

def raw_positions():
    """raw robinhood positions."""

    return StockPosition.all(rh_client())

def raw_stock(symbol, attributes=None):
    """raw robinhood stock infos. not personal position on the stock.

    if attributes is passed along, only return those attributes.
    """

    stock = Stock.fetch(rh_client(), symbol)

    if attributes is not None:
        return {k: stock[k] for k in attributes}

    return stock

def raw_stocks(symbols):
    """raw robinhood stock infos."""

    stocks = Stock.all(rh_client(), symbols)

    return stocks

def rh_id_from_instrument_url(url):
    """get the RH id from the instrument url. needed to look up stock data."""

    tokens = url.split("/")

    return tokens[4]

def list_to_row(input_list):
    """convenience method to take a list and return it as a comma-separated list."""

    row = ''

    for value in input_list:
        row += str(value) + ','

    row += '\n'
    return row

def rh_positions(csv=False):
    """my portfolio positions. formatted for personal use in Google Sheets."""

    positions = raw_positions()
    instrument_urls = list(map(lambda p: p['instrument'], positions))

    instrument_data = {}
    for url in instrument_urls:
        data = rh_client().get(url)
        instrument_data[data['id']] = data

    formatted_positions = {}
    for position in positions:
        if float(position['quantity']) == 0.0:
            continue

        item = {}

        for k in ['average_buy_price', 'created_at', 'quantity']:
            item[k] = position[k]

        rh_id = rh_id_from_instrument_url(position['instrument'])

        data = instrument_data[rh_id]
        for k in ['simple_name', 'symbol', 'type']:
            item[k] = data[k]

        quote = raw_quote(item['symbol'])

        for k in [
                'adjusted_previous_close',
                'ask_price',
                'bid_price',
                'last_trade_price',
                'last_extended_hours_trade_price',
                'last_trade_price',
                'previous_close',
            ]:
            item[k] = quote[k]

        formatted_positions[item['symbol']] = item

    if csv is not False:
        row = ''
        i = 0
        for item in list(formatted_positions.values()):
            if i == 0:
                row += list_to_row(item.keys())

            row += list_to_row(item.values())
            i += 1

        return row

    return jsonify(formatted_positions)

def raw_collection(tag):
    """raw robinhood collection info via fast_arrow."""

    return Collection.fetch_instruments_by_tag(rh_client(), tag)

def rh_collection(tag):
    """rh collection. formatted for personal use"""

    return jsonify(raw_collection(tag))

def raw_quote(symbol, attributes=None):
    """raw market price quote info via fast_arrow."""

    quote = StockMarketdata.quote_by_symbol(rh_client(), symbol)

    if attributes is not None:
        return {k: quote[k] for k in attributes}

    return quote

def rh_quote(symbol):
    """formatted price quote infos for personal use."""

    quote = raw_quote(symbol, [
        "last_trade_price"
    ])

    return jsonify(quote)

def raw_watchlist():
    """raw watchlist infos."""

def rh_watchlist():
    """my watchlist. formatted position list."""

    return jsonify(raw_watchlist())
