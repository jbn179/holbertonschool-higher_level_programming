#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiply all values in a list by a given number.

    Parameters:
    my_list (list): The list of values to multiply.
    number (int): The number to multiply by.

    Returns:
    list: The list of multiplied values.
    """
    return list(map(lambda x: x * number, my_list))
