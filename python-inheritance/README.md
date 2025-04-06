# Python Inheritance 🧬

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OOP](https://img.shields.io/badge/OOP-Inheritance-green.svg)

## 📖 Description
This project explores inheritance in Python's object-oriented programming paradigm. Inheritance allows classes to adopt attributes and methods from parent classes, promoting code reuse and establishing relationships between classes. The project demonstrates single inheritance, multiple inheritance, method overriding, and various ways to inspect and utilize class hierarchies.

## 📂 Contents
- **0-lookup.py**: Returns the list of available attributes and methods of an object
- **1-my_list.py**: Creates a list subclass with a sorted printing method
- **2-is_same_class.py**: Checks if an object is exactly an instance of a specified class
- **3-is_kind_of_class.py**: Checks if an object is an instance of, or inherited from, a specified class
- **4-inherits_from.py**: Checks if an object is an instance of a class that inherited from a specified class
- **5-base_geometry.py**: Creates an empty BaseGeometry class
- **6-base_geometry.py**: Adds an area method that raises an exception
- **7-base_geometry.py**: Adds integer validation to the BaseGeometry class
- **8-rectangle.py**: Creates a Rectangle class that inherits from BaseGeometry
- **9-rectangle.py**: Adds area implementation and string representation to Rectangle
- **10-square.py**: Creates a Square class that inherits from Rectangle
- **11-square.py**: Adds proper string representation to the Square class
- **tests/**: Directory containing test files for the project

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-inheritance
   ```

3. Run the Python scripts:
   ```bash
   python3 0-main.py
   ```

## 🛠️ Requirements
- Python 3.8+
- Ubuntu 20.04 LTS
- pycodestyle 2.8.* (PEP 8 style)
- All modules, classes, and functions must include docstrings

## Key Concepts ✨
- **Inheritance**: Mechanism for code reuse where a class adopts attributes/methods from another class
- **Base Class**: The class being inherited from (parent or superclass)
- **Derived Class**: The class that inherits from another class (child or subclass)
- **Method Overriding**: Redefining a method in a subclass that exists in the parent class
- **super()**: Function to call methods from the parent class
- **isinstance()**: Function to check if an object is an instance of a class
- **issubclass()**: Function to check if a class is a subclass of another class
- **Multiple Inheritance**: Inheriting from more than one class

## Examples

### Simple Inheritance
```python
#!/usr/bin/python3
"""Simple inheritance example with a Rectangle class"""


class BaseGeometry:
    """Base class for geometry-related classes"""
    def area(self):
        """Method that calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


# Usage
r = Rectangle(5, 7)
print(r)  # [Rectangle] 5/7
print(r.area())  # 35
```

### Checking Instance Types
```python
#!/usr/bin/python3
"""Functions to check instance relationships"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of specified class"""
    return type(obj) is a_class


def is_kind_of_class(obj, a_class):
    """Check if object is instance of or inherits from specified class"""
    return isinstance(obj, a_class)


def inherits_from(obj, a_class):
    """Check if object is instance of a class that inherited from a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


# Usage
a = 1
print(is_same_class(a, int))  # True
print(is_same_class(a, float))  # False
print(is_kind_of_class(a, int))  # True
print(is_kind_of_class(a, object))  # True
print(inherits_from(a, object))  # True
print(inherits_from(a, int))  # False
```

## Testing
The project includes a comprehensive test suite to verify all functionality:

```bash
python3 -m doctest ./tests/7-base_geometry.txt
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author ✍️
- Benjamin Ristord