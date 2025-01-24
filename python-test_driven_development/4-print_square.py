#!/usr/bin/python3

def print_square(size):
    """
    Print a square with the '#' character.

    Parameters:
    size (int): The size length of the square (number of '#' per side).

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.

    Note:
    If size is a float and less than 0, raise a TypeError with the same
    message as for non-int types.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
