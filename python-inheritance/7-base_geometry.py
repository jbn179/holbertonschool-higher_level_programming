#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Method that raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates if a value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
