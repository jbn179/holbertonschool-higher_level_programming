#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (only once for each integer).

    Parameters:
    my_list (list): The list of integers.

    Returns:
    int: The sum of all unique integers in the list.
    """
    return sum(set(my_list))
