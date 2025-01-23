#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print the first x elements of a list safely.

    Parameters:
    my_list (list): The list to print elements from.
    x (int): The number of elements to print.

    Returns:
    int: The actual number of elements printed.
    """
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except IndexError:
        print()
        return i
 