#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element by another in a list.

    Parameters:
    my_list (list): The list to search and replace elements in.
    search: The element to search for in the list.
    replace: The element to replace the searched element with.

    Returns:
    list: A new list with the searched elements replaced by the new element.
    """
    return [replace if i == search else i for i in my_list]
