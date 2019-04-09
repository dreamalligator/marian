from lazy_money_maker.utils.sheets import list_to_row

def test_list_to_row():
    expected_row = 'junk,None,1,https://charliecat.net\n'
    assert list_to_row(['junk', None, 1, 'https://charliecat.net'] == expected_row)
