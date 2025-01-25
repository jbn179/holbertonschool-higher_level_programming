# 📚 Python Exceptions

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description
This repository contains Python scripts and programs that demonstrate the use of exceptions. The goal is to provide a comprehensive understanding of how to handle errors and exceptions in Python. Each script is designed to be simple and easy to understand, making them ideal for learners who are looking to deepen their knowledge of Python exception handling.

The scripts cover a range of topics, including:
- Basic try/except blocks
- Handling multiple exceptions
- Using else and finally clauses
- Raising exceptions
- Custom exception classes

## 📂 Contents
- **0-safe_print_list.py**: Prints x elements of a list.
- **1-safe_print_integer.py**: Prints an integer with "{:d}".format().
- **2-safe_print_list_integers.py**: Prints the first x elements of a list and only integers.
- **3-safe_print_division.py**: Divides 2 integers and prints the result.
- **4-list_division.py**: Divides element by element 2 lists.
- **5-raise_exception.py**: Raises a type exception.
- **6-raise_exception_msg.py**: Raises a name exception with a message.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-exceptions
   ```
3. Run each script:
   ```bash
   python3 0-safe_print_list.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-safe_print_list.py
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

### 1-safe_print_integer.py
Prints an integer with "{:d}".format():
```python
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

print(safe_print_integer(42))
# Output: 42
# True
```

### 2-safe_print_list_integers.py
Prints the first x elements of a list and only integers:
```python
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count

print(safe_print_list_integers([1, "a", 2, "b", 3], 5))
# Output:
# 123
# 3
```

### 3-safe_print_division.py
Divides 2 integers and prints the result:
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

### 4-list_division.py
Divides element by element 2 lists:
```python
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list

print(list_division([10, 20, 30], [2, 0, "a"], 3))
# Output:
# [5.0, 0, 0]
```

### 5-raise_exception.py
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

### 6-raise_exception_msg.py
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