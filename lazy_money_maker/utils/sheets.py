'''
Google Sheets or CSV-type related utils
'''

def list_to_row(input_list):
    """convenience method to take a list and return it as a comma-separated list."""

    row = ''

    # using for-loop over join to accomodate coercing possible NoneTypes
    for value in input_list:
        row += str(value) + ','

    row += '\n'
    return row
