#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the maximum integer in a list.

    Parameters:
    my_list (list): The list of integers to search.

    Returns:
    int: The maximum integer in the list. If the list is empty, returns None.
    """
    if not my_list:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
