#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary with its keys in sorted order.

    Parameters:
    a_dictionary (dict): The dictionary to print.

    Returns:
    None
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
