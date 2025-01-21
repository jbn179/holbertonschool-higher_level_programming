#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Parameters:
    my_list (list): The list of integers to print in reverse order.
    """
    if my_list is not None:
        for i in reversed(my_list):
            print("{:d}".format(i))
