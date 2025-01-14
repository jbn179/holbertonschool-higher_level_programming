#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Create a copy of the string, removing the character at the position n.

    Parameters:
    str (str): The original string.
    n (int): The position of the character to remove.

    Returns:
    str: The new string with the character at position n removed.
    """
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]
