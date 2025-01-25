# 📚 Python Test-Driven Development

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Tests](https://img.shields.io/badge/Tests-passing-brightgreen.svg)

## 📖 Description
This repository demonstrates Python Test-Driven Development (TDD) practices. TDD is a software development process where tests are written before the code itself. This approach ensures that the code is thoroughly tested and meets the specified requirements. Each script in this repository is accompanied by tests that validate its functionality.

The scripts cover a range of topics, including:
- Basic arithmetic operations
- Matrix manipulation
- String formatting and printing
- Handling exceptions
- Writing and running unittests

These examples are intended to be simple and easy to understand, making them ideal for new programmers who are just starting out with Python and TDD.

## 📂 Contents
- **0-add_integer.py**, tests/0-add_integer.txt  
- **2-matrix_divided.py**, tests/2-matrix_divided.txt  
- **3-say_my_name.py**, tests/3-say_my_name.txt  
- **4-print_square.py**, tests/4-print_square.txt  
- **5-text_indentation.py**, tests/5-text_indentation.txt  
- **6-max_integer.py**, tests/6-max_integer_test.py

## 🚀 Quick Start
1. Clone the repo:
   ```bash
   git clone https://github.com/username/repo_name.git
   ```
2. Run unittests:
   ```bash
   python3 -m unittest tests
   ```
3. Run doctests for one file:
   ```bash
   python3 -m doctest -v ./tests/0-add_integer.txt
   ```

## 🛠️ Requirements
• Python 3.8+  
• No external libraries allowed

---

## Examples & Tests

### 0-add_integer
**Usage**:  
```python
from 0_add_integer import add_integer
print(add_integer(4.5, 1))  # 5
print(add_integer(4))       # 102
```
**Doctest** (`tests/0-add_integer.txt`):  
```txt
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100.3, -2)
98
>>> add_integer("4", 2)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
```

### 2-matrix_divided
**Usage**:  
```python
from 2_matrix_divided import matrix_divided
matrix = [[4, 8], [2, 6]]
print(matrix_divided(matrix, 2))
# [[2.0, 4.0], [1.0, 3.0]]
```
**Doctest** (`tests/2-matrix_divided.txt`):  
```txt
>>> matrix_divided = __import__('2_matrix_divided').matrix_divided
>>> matrix_divided([[4, 8], [2, 6]], 2)
[[2.0, 4.0], [1.0, 3.0]]
>>> matrix_divided([], 2)
[]
>>> matrix_divided("not a list", 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats
```

### 3-say_my_name
**Usage**:  
```python
from 3_say_my_name import say_my_name
say_my_name("John", "Doe")
# My name is John Doe
```
**Doctest** (`tests/3-say_my_name.txt`):  
```txt
>>> say_my_name = __import__('3_say_my_name').say_my_name
>>> say_my_name("Walter", "White")
My name is Walter White
>>> say_my_name(123, "White")
Traceback (most recent call last):
    ...
TypeError: first_name must be a string
```

### 4-print_square
**Usage**:  
```python
from 4_print_square import print_square
print_square(3)
# ###
# ###
# ###
```
**Doctest** (`tests/4-print_square.txt`):  
```txt
>>> print_square = __import__('4_print_square').print_square
>>> print_square(2)
##
##
>>> print_square(0)

>>> print_square(-1)
Traceback (most recent call last):
    ...
ValueError: size must be >= 0
>>> print_square("4")
Traceback (most recent call last):
    ...
TypeError: size must be an integer
```

### 5-text_indentation
**Usage**:  
```python
from 5_text_indentation import text_indentation
text = "Hello. World? Example: text."
text_indentation(text)
# Hello.
#
# World?
#
# Example:
#
# text.
```
**Doctest** (`tests/5-text_indentation.txt`):  
```txt
>>> text_indentation = __import__('5_text_indentation').text_indentation
>>> text_indentation("Hello.  World?")
Hello.
<BLANKLINE>
World?
<BLANKLINE>
>>> text_indentation("")
>>> text_indentation(123)
Traceback (most recent call last):
    ...
TypeError: text must be a string
```

### 6-max_integer
**Usage**:  
```python
from 6_max_integer import max_integer
print(max_integer([1, 3, 10, 2]))
# 10
```
**Unittest** (`tests/6-max_integer_test.py`):  
```python
#!/usr/bin/python3
"""Unittest for max_integer([...])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -1]), -1)

if __name__ == '__main__':
    unittest.main()
```

---

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
• Benjamin Ristord - [@jbn179](https://github.com/jbn179)
