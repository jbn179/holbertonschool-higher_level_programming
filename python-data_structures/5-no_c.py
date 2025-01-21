#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from a string.

    Parameters:
    my_string (str): The original string.

    Returns:
    str: The new string with all 'c' and 'C' characters removed.
    """
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
