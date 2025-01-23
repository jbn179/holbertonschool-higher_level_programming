#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list containing only integers.

    Parameters:
    my_list (list): The list to print elements from.
    x (int): The number of elements to print.

    Returns:
    int: The actual number of elements printed.
    """
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return printed
