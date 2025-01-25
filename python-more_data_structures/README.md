# 📚 Python More Data Structures

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description
This repository contains Python scripts and programs that demonstrate advanced data structures and algorithms. The goal is to provide a deeper understanding of how to implement and use different data structures in Python, including sets, dictionaries, and more complex operations. Each script is designed to be simple and easy to understand, making them ideal for learners who are looking to deepen their knowledge of Python data structures.

The scripts cover a range of topics, including:
- Advanced list operations
- Set operations
- Dictionary usage
- Lambda functions and map/filter/reduce
- Implementing algorithms with data structures

## 📂 Contents
- **0-square_matrix_simple.py**: Computes the square value of all integers of a matrix.
- **1-search_replace.py**: Replaces all occurrences of an element by another in a new list.
- **2-uniq_add.py**: Adds all unique integers in a list.
- **3-common_elements.py**: Returns a set of common elements in two sets.
- **4-only_diff_elements.py**: Returns a set of all elements present in only one set.
- **5-number_keys.py**: Returns the number of keys in a dictionary.
- **6-print_sorted_dictionary.py**: Prints a dictionary by ordered keys.
- **7-update_dictionary.py**: Replaces or adds key/value in a dictionary.
- **8-simple_delete.py**: Deletes a key in a dictionary.
- **9-multiply_by_2.py**: Returns a new dictionary with all values multiplied by 2.
- **10-best_score.py**: Returns a key with the biggest integer value.
- **11-multiply_list_map.py**: Returns a list with all values multiplied by a number without using any loops.
- **12-roman_to_int.py**: Converts a Roman numeral to an integer.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-more_data_structures
   ```
3. Run each script:
   ```bash
   python3 0-square_matrix_simple.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-square_matrix_simple.py
Computes the square value of all integers of a matrix:
```python
from 0_square_matrix_simple import square_matrix_simple
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(square_matrix_simple(matrix))
# Output:
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

### 1-search_replace.py
Replaces all occurrences of an element by another in a new list:
```python
from 1_search_replace import search_replace
my_list = [1, 2, 3, 4, 3]
new_list = search_replace(my_list, 3, 9)
print(new_list)
# Output: [1, 2, 9, 4, 9]
```

### 2-uniq_add.py
Adds all unique integers in a list:
```python
from 2_uniq_add import uniq_add
print(uniq_add([1, 2, 3, 1, 4, 2, 5]))
# Output: 15
```

### 3-common_elements.py
Returns a set of common elements in two sets:
```python
from 3_common_elements import common_elements
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
print(common_elements(set_1, set_2))
# Output: {2, 3}
```

### 4-only_diff_elements.py
Returns a set of all elements present in only one set:
```python
from 4_only_diff_elements import only_diff_elements
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
print(only_diff_elements(set_1, set_2))
# Output: {1, 4}
```

### 5-number_keys.py
Returns the number of keys in a dictionary:
```python
from 5_number_keys import number_keys
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
print(number_keys(a_dictionary))
# Output: 3
```

### 6-print_sorted_dictionary.py
Prints a dictionary by ordered keys:
```python
from 6_print_sorted_dictionary import print_sorted_dictionary
a_dictionary = {'b': 2, 'a': 1, 'c': 3}
print_sorted_dictionary(a_dictionary)
# Output:
# a: 1
# b: 2
# c: 3
```

### 7-update_dictionary.py
Replaces or adds key/value in a dictionary:
```python
from 7_update_dictionary import update_dictionary
a_dictionary = {'a': 1, 'b': 2}
update_dictionary(a_dictionary, 'c', 3)
print(a_dictionary)
# Output: {'a': 1, 'b': 2, 'c': 3}
```

### 8-simple_delete.py
Deletes a key in a dictionary:
```python
from 8_simple_delete import simple_delete
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
simple_delete(a_dictionary, 'b')
print(a_dictionary)
# Output: {'a': 1, 'c': 3}
```

### 9-multiply_by_2.py
Returns a new dictionary with all values multiplied by 2:
```python
from 9_multiply_by_2 import multiply_by_2
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
print(multiply_by_2(a_dictionary))
# Output: {'a': 2, 'b': 4, 'c': 6}
```

### 10-best_score.py
Returns a key with the biggest integer value:
```python
from 10_best_score import best_score
a_dictionary = {'a': 1, 'b': 2, 'c': 3}
print(best_score(a_dictionary))
# Output: 'c'
```

### 11-multiply_list_map.py
Returns a list with all values multiplied by a number without using any loops:
```python
from 11_multiply_list_map import multiply_list_map
my_list = [1, 2, 3, 4]
new_list = multiply_list_map(my_list, 2)
print(new_list)
# Output: [2, 4, 6, 8]
```

### 12-roman_to_int.py
Converts a Roman numeral to an integer:
```python
from 12_roman_to_int import roman_to_int
print(roman_to_int("XIV"))
# Output: 14
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)