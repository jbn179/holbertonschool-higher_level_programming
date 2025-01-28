#!/usr/bin/python3
"""This module defines a class Square that defines a square by its size."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with a private instance attribute size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
