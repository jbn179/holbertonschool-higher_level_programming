#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific index.

    Parameters:
    my_list (list): The list in which to replace the element.
    idx (int): The index at which to replace the element.
    element (int): The element to replace.

    Returns:
    The modified list.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
