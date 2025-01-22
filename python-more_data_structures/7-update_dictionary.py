#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Parameters:
    a_dictionary (dict): The dictionary to update.
    key (any): The key to update or add.
    value (any): The value to update or add.

    Returns:
    dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
