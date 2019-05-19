from marian.utils.sheets import list_to_row

def test_list_to_row():
    expected_row = 'junk,None,1,True,False,https://charliecat.net\n'
    input_list = ['junk', None, 1, True, False, 'https://charliecat.net']
    assert list_to_row(input_list) == expected_row
