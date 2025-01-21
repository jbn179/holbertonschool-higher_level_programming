#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.

    Parameters:
    tuple_a (tuple): The first tuple. Defaults to an empty tuple.
    tuple_b (tuple): The second tuple. Defaults to an empty tuple.

    Returns:
    tuple: A tuple containing the element-wise sum of the first two elements
           of the input tuples.
           If a tuple has less than 2 elements, 0 is used as the missing value.
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return tuple(map(lambda x, y: x + y, tuple_a[:2], tuple_b[:2]))
