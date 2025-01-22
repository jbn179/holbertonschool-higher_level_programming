#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements present in only one of the sets.

    Parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.

    Returns:
    set: A set of elements that are present in only one of the sets.
    """
    return set_1 ^ set_2
