#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add two integers.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number, default is 98.

    Returns:
    int: The sum of a and b, casted to integers.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
