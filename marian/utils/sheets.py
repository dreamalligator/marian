'''
Google Sheets or CSV-type related utils
'''

def list_to_row(input_list):
    """convenience method to take a list and return it as a comma-separated list."""

    row = ''
    i = 0
    # using for-loop over join to accomodate coercing possible NoneTypes with str.
    for value in input_list:
        row += str(value)

        if i < len(input_list) - 1:
            row += ','

        i += 1

    row += '\n'
    return row
