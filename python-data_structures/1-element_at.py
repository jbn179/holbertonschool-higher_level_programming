#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specific index.

    Parameters:
    my_list (list): The list from which to retrieve the element.
    idx (int): The index of the element to retrieve.

    Returns:
    The element at the specified index if the index is valid, otherwise None.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
