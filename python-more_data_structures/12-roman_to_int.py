#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Parameters:
    roman_string (str): The Roman numeral string to convert.

    Returns:
    int: The integer representation of the Roman numeral.
    If the input is not a string or is None, returns 0.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = 0

    for i in roman_string:
        if roman_dict[i] > prev:
            num += roman_dict[i] - 2 * prev
        else:
            num += roman_dict[i]
        prev = roman_dict[i]
    return num
