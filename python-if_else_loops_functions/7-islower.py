#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.

    Parameters:
    c (str): The character to check.

    Returns:
    bool: True if c is lowercase, False otherwise.
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')
