# 📚 Python More Classes

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description 
This repository contains Python scripts and programs that demonstrate the use of classes and object-oriented programming (OOP) concepts. The goal is to provide a comprehensive understanding of how to define and use classes in Python, including attributes, methods, and encapsulation. Each script is designed to be simple and easy to understand, making them ideal for learners who are looking to deepen their knowledge of Python OOP.

The projects cover a range of topics, including:
- Defining classes and creating objects
- Using instance and class attributes
- Implementing methods
- Encapsulation and data hiding
- Property decorators for getters and setters

## 📂 Contents
- **0-rectangle.py**: Defines an empty class `Rectangle`.
- **1-rectangle.py**: Defines a class `Rectangle` with private instance attributes `width` and `height`.
- **2-rectangle.py**: Adds validation for the `width` and `height` attributes.
- **3-rectangle.py**: Adds a public instance method `area` to calculate the area of the rectangle.
- **4-rectangle.py**: Adds a public instance method `perimeter` to calculate the perimeter of the rectangle.
- **5-rectangle.py**: Adds a `__str__` method to print the rectangle with the `#` character.
- **6-rectangle.py**: Adds a `__repr__` method to provide a string representation of the rectangle.
- **7-rectangle.py**: Adds a class attribute `number_of_instances` to keep track of the number of instances.
- **8-rectangle.py**: Adds a class attribute `print_symbol` to customize the symbol used for string representation.
- **9-rectangle.py**: Adds a static method `bigger_or_equal` to compare the areas of two rectangles.
- **10-square.py**: Defines a class `Square` that inherits from `Rectangle`.

## 🚀 Getting Started
1. Clone the repository to access the materials:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the `python-more_classes` directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-more_classes
   ```
3. Run the Python scripts:
   ```bash
   python3 0-rectangle.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-rectangle.py
Defines an empty class `Rectangle`:
```python
class Rectangle:
    """An empty class that defines a rectangle."""
    pass
```

### 1-rectangle.py
Defines a class `Rectangle` with private instance attributes `width` and `height`:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.__width = width
        self.__height = height
```

### 2-rectangle.py
Adds validation for the `width` and `height` attributes:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with type and value validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with type and value validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
```

### 3-rectangle.py
Adds a public instance method `area` to calculate the area of the rectangle:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
```

### 4-rectangle.py
Adds a public instance method `perimeter` to calculate the perimeter of the rectangle:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
```

### 5-rectangle.py
Adds a `__str__` method to print the rectangle with the `#` character:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of the rectangle with the `#` character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
```

### 6-rectangle.py
Adds a `__repr__` method to provide a string representation of the rectangle:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
```

### 7-rectangle.py
Adds a class attribute `number_of_instances` to keep track of the number of instances:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance is deleted and decrement the instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
```

### 8-rectangle.py
Adds a class attribute `print_symbol` to customize the symbol used for string representation:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string representation of the rectangle with the `print_symbol` character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])
```

### 9-rectangle.py
Adds a static method `bigger_or_equal` to compare the areas of two rectangles:
```python
class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with private instance attributes width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
```

### 10-square.py
Defines a class `Square` that inherits from `Rectangle`:
```python
@classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with
        width and height equal to size."""
        return cls(size, size)
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)
