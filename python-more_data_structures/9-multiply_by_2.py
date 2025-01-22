#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.

    Parameters:
    a_dictionary (dict): The dictionary to process.

    Returns:
    dict: A new dictionary with all values multiplied by 2.
    """
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= 2
    return new_dict
