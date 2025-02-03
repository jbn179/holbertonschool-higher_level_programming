from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    Defines methods that any shape must implement.
    """

    @abstractmethod
    def __init__(self):
        """Initialization method for shapes."""
        pass

    @abstractmethod
    def area(self):
        """
        Compute the shape's area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the shape's perimeter.
        """
        pass


class Circle(Shape):
    """
    Represents a circle defined by its radius.
    """

    def __init__(self, radius=0):
        """
        Initialize the circle with a specific radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the circle's area using πr².
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the circle's perimeter using 2πr.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle defined by its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with a specific width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the rectangle's area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the rectangle's perimeter.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): An instance of a class that implements
        the Shape interface.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
