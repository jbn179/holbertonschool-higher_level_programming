#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position without modifying the original list.

    Parameters:
    my_list (list): The list to replace an element in.
    idx (int): The index of the element to replace.
    element (int): The new element to replace the old element with.

    Returns:
    list: The new list with the element replaced.
    """
    if my_list is not None:
        new_list = my_list.copy()
        if 0 <= idx < len(new_list):
            new_list[idx] = element
        return new_list
    return None
