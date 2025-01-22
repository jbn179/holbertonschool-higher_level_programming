#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Parameters:
    my_list (list): A list of integers.

    Returns:
    A list of booleans.
    """
    return [True if i % 2 == 0 else False for i in my_list]
