
# 📚 Python Data Structures

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description
This repository contains Python scripts and programs that demonstrate various data structures and algorithms. The goal is to provide a comprehensive understanding of how to implement and use different data structures in Python, including lists, tuples, sets, and dictionaries. Each script is designed to be simple and easy to understand, making them ideal for learners who are looking to deepen their knowledge of Python data structures.

The scripts cover a range of topics, including:
- Basic list operations
- Tuple manipulation
- Set operations
- Dictionary usage
- Implementing algorithms with data structures

## 📂 Contents
- **0-print_list_integer.py**: Prints all integers of a list.
- **1-element_at.py**: Retrieves an element from a list.
- **2-replace_in_list.py**: Replaces an element in a list at a specific position.
- **3-print_reversed_list_integer.py**: Prints all integers of a list, in reverse order.
- **4-new_in_list.py**: Replaces an element in a list at a specific position without modifying the original list.
- **5-no_c.py**: Removes all characters 'c' and 'C' from a string.
- **6-print_matrix_integer.py**: Prints a matrix of integers.
- **7-add_tuple.py**: Adds two tuples.
- **8-multiple_returns.py**: Returns a tuple with the length of a string and its first character.
- **9-max_integer.py**: Finds the biggest integer of a list.
- **10-divisible_by_2.py**: Finds all multiples of 2 in a list.
- **11-delete_at.py**: Deletes the item at a specific position in a list.
- **12-switch.py**: Switches the values of two variables.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-data_structures
   ```
3. Run each script:
   ```bash
   python3 0-print_list_integer.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-print_list_integer.py
Prints all integers of a list:
```python
from 0_print_list_integer import print_list_integer
print_list_integer([1, 2, 3, 4, 5])
# Output:
# 1
# 2
# 3
# 4
# 5
```

### 1-element_at.py
Retrieves an element from a list:
```python
from 1_element_at import element_at
print(element_at([1, 2, 3, 4, 5], 2))
# Output: 3
```

### 2-replace_in_list.py
Replaces an element in a list at a specific position:
```python
from 2_replace_in_list import replace_in_list
print(replace_in_list([1, 2, 3, 4, 5], 2, 9))
# Output: [1, 2, 9, 4, 5]
```

### 3-print_reversed_list_integer.py
Prints all integers of a list, in reverse order:
```python
from 3_print_reversed_list_integer import print_reversed_list_integer
print_reversed_list_integer([1, 2, 3, 4, 5])
# Output:
# 5
# 4
# 3
# 2
# 1
```

### 4-new_in_list.py
Replaces an element in a list at a specific position without modifying the original list:
```python
from 4_new_in_list import new_in_list
print(new_in_list([1, 2, 3, 4, 5], 2, 9))
# Output: [1, 2, 9, 4, 5]
```

### 5-no_c.py
Removes all characters 'c' and 'C' from a string:
```python
from 5_no_c import no_c
print(no_c("Holberton School"))
# Output: Holberton Shool
```

### 6-print_matrix_integer.py
Prints a matrix of integers:
```python
from 6_print_matrix_integer import print_matrix_integer
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### 7-add_tuple.py
Adds two tuples:
```python
from 7_add_tuple import add_tuple
print(add_tuple((1, 2), (3, 4)))
# Output: (4, 6)
```

### 8-multiple_returns.py
Returns a tuple with the length of a string and its first character:
```python
from 8_multiple_returns import multiple_returns
print(multiple_returns("Holberton"))
# Output: (9, 'H')
```

### 9-max_integer.py
Finds the biggest integer of a list:
```python
from 9_max_integer import max_integer
print(max_integer([1, 2, 3, 4, 5]))
# Output: 5
```

### 10-divisible_by_2.py
Finds all multiples of 2 in a list:
```python
from 10_divisible_by_2 import divisible_by_2
print(divisible_by_2([1, 2, 3, 4, 5]))
# Output: [False, True, False, True, False]
```

### 11-delete_at.py
Deletes the item at a specific position in a list:
```python
from 11_delete_at import delete_at
print(delete_at([1, 2, 3, 4, 5], 2))
# Output: [1, 2, 4, 5]
```

### 12-switch.py
Switches the values of two variables:
```python
from 12_switch import switch
a, b = switch(1, 2)
print(a, b)
# Output: 2 1
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
• Benjamin Ristord - [@jbn179](https://github.com/jbn179)