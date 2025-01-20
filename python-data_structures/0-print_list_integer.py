#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Print all integers of a list.

    Parameters:
    my_list (list): A list of integers.

    Returns:
    None
    """
    for i in my_list:
        print("{:d}".format(i))
