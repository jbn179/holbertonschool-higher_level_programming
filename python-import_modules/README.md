# 📚 Python Import & Modules

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description
This repository contains Python scripts and programs that demonstrate the use of import statements and modules. The goal is to provide a comprehensive understanding of how to import and use modules in Python, including built-in modules, standard library modules, and custom modules. Each script is designed to be simple and easy to understand, making them ideal for learners who are looking to deepen their knowledge of Python modules and imports.

The scripts cover a range of topics, including:
- Importing modules
- Using functions from imported modules
- Creating and using custom modules
- Understanding module search paths
- Using the `__import__` function

## 📂 Contents
- **0-add.py**: Imports a function from a file and prints the result.
- **1-args.py**: Prints the number of and the list of its arguments.
- **2-variable_load.py**: Imports a variable from a file and prints its value.
- **3-safe_print_division.py**: Divides two integers and prints the result.
- **4-raise_exception.py**: Raises a type exception.
- **5-raise_exception_msg.py**: Raises a name exception with a message.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-import_modules
   ```
3. Run each script:
   ```bash
   python3 0-add.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-add.py
Imports a function from a file and prints the result:
```python
from add_0 import add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
# Output: 1 + 2 = 3
```

### 1-args.py
Prints the number of and the list of its arguments:
```python
import sys
print("{} argument(s):".format(len(sys.argv) - 1))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
# Output (if run with "python3 1-args.py arg1 arg2"):
# 2 argument(s):
# 1: arg1
# 2: arg2
```

### 2-variable_load.py
Imports a variable from a file and prints its value:
```python
from variable_load_2 import a
print(a)
# Output: (value of variable 'a' from variable_load_2.py)
```

### 3-safe_print_division.py
Divides two integers and prints the result:
```python
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

print(safe_print_division(10, 2))
# Output:
# Inside result: 5.0
# 5.0
```

### 4-raise_exception.py
Raises a type exception:
```python
def raise_exception():
    raise TypeError("This is a type exception")

try:
    raise_exception()
except TypeError as e:
    print(e)
# Output: This is a type exception
```

### 5-raise_exception_msg.py
Raises a name exception with a message:
```python
def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg("This is a name exception")
except NameError as e:
    print(e)
# Output: This is a name exception
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)