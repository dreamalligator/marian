from marian.utils.robinhood import rh_id_from_instrument_url

def test_rh_id_from_instrument_url():
    instrument_url = 'https://api.robinhood.com/instruments/5f212925-bb37-494b-ae03-deb40f0fb2e3/'
    expected_instrument_id = '5f212925-bb37-494b-ae03-deb40f0fb2e3'
    assert rh_id_from_instrument_url(instrument_url) == expected_instrument_id
