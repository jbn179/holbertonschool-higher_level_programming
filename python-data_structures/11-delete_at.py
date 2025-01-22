#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete an element from a list at a specific position.

    Parameters:
    my_list (list): The list from which to delete an element.
    idx (int): The index of the element to delete.

    Returns:
    list: The modified list with the element deleted.
    If the index is invalid, returns the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
