#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary.

    Parameters:
    a_dictionary (dict): The dictionary to delete from.
    key (any): The key to delete.

    Returns:
    dict: The modified dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
