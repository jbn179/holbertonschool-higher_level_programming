# 📚 Holberton School Higher Level Programming

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description
This repository contains a collection of Python scripts and programs developed as part of the Holberton School Higher Level Programming curriculum. The goal is to provide a comprehensive understanding of various programming concepts and techniques using Python. Each directory within this repository focuses on a specific topic or project, designed to build and enhance your programming skills.

The projects cover a range of topics, including:
- Basic syntax and data structures
- Control flow and functions
- Importing and using modules
- Error handling and exceptions
- Object-oriented programming
- Advanced data structures and algorithms

## 📂 Contents
- **python-hello_world**: Introduction to Python programming.
- **python-if_else_loops_functions**: Control flow and functions.
- **python-import_modules**: Importing and using modules.
- **python-data_structures**: Basic data structures.
- **python-more_data_structures**: Advanced data structures.
- **python-exceptions**: Error handling and exceptions.
- **python-test_driven_development**: Writing and running tests.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the desired directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-hello_world
   ```
3. Run the scripts:
   ```bash
   python3 2-print.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### python-hello_world
Prints a string to stdout:
```python
print("Programming is like building a multilingual puzzle")
# Output: Programming is like building a multilingual puzzle
```

### python-if_else_loops_functions
Prints whether a number is positive, negative, or zero:
```python
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
```

### python-import_modules
Imports a function from a file and prints the result:
```python
from add_0 import add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
# Output: 1 + 2 = 3
```

### python-data_structures
Prints all integers of a list:
```python
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))

print_list_integer([1, 2, 3, 4, 5])
# Output:
# 1
# 2
# 3
# 4
# 5
```

### python-more_data_structures
Computes the square value of all integers of a matrix:
```python
def square_matrix_simple(matrix=[]):
    return [[x ** 2 for x in row] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(square_matrix_simple(matrix))
# Output:
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

### python-exceptions
Prints x elements of a list:
```python
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count

print(safe_print_list([1, 2, 3, 4, 5], 3))
# Output:
# 123
# 3
```

### python-test_driven_development
Adds two integers or floats, returns int:
```python
from 0_add_integer import add_integer
print(add_integer(4.5, 1))  # 5
print(add_integer(4))       # 102
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)