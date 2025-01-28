# 📚 Python Classes

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
- **0-square.py**: Defines an empty class `Square`.
- **1-square.py**: Defines a class `Square` with a private instance attribute `size`.
- **2-square.py**: Adds validation for the `size` attribute.
- **3-square.py**: Adds a public instance method `area` to calculate the area of the square.
- **4-square.py**: Adds property decorators for the `size` attribute.
- **5-square.py**: Adds a public instance method `my_print` to print the square.
- **6-square.py**: Adds a private instance attribute `position` with validation and a method to print the square with position.

## 🚀 Getting Started
1. Clone the repository to access the materials:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the `python-classes` directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-classes
   ```
3. Run the Python scripts:
   ```bash
   python3 0-square.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-square.py
Defines an empty class `Square`:
```python
class Square:
    """An empty class that defines a square."""
    pass
```

### 1-square.py
Defines a class `Square` with a private instance attribute `size`:
```python
class Square:
    """A class that defines a square by its size."""
    
    def __init__(self, size):
        """Initialize the square with a private instance attribute size."""
        self.__size = size
```

### 2-square.py
Adds validation for the `size` attribute:
```python
class Square:
    """A class that defines a square by its size."""
    
    def __init__(self, size=0):
        """Initialize the square with a private instance attribute size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
```

### 3-square.py
Adds a public instance method `area` to calculate the area of the square:
```python
class Square:
    """A class that defines a square by its size."""
    
    def __init__(self, size=0):
        """Initialize the square with a private instance attribute size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
```

### 4-square.py
Adds property decorators for the `size` attribute:
```python
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
```

### 5-square.py
Adds a public instance method `my_print` to print the square:
```python
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
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
```

### 6-square.py
Adds a private instance attribute `position` with validation and a method to print the square with position:
```python
class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a private instance attribute size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type and value validation."""
        if (type(value) is not tuple or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)
