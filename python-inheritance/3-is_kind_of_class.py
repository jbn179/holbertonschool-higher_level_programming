#!/usr/bin/python3
"""Module that checks if an object is an instance of a class
or a subclass."""


def is_kind_of_class(obj, a_class):
    """Function that checks if an object is an instance of a class
    or a subclass."""
    return isinstance(obj, a_class)
