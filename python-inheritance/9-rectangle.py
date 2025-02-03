#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Return string representation of rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height
