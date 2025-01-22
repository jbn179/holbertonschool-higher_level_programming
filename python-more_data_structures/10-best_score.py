#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the highest integer value in a dictionary.

    Parameters:
    a_dictionary (dict): The dictionary to search. Keys are strings and values are integers.

    Returns:
    str: The key with the highest integer value. If the dictionary is empty or None, returns None.
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    return max(a_dictionary, key=a_dictionary.get)
