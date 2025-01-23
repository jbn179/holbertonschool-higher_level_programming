#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer safely.

    Parameters:
    value (int): The integer to print.

    Returns:
    bool: True if the integer was printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
