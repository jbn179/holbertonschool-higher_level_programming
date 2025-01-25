# 📚 Python If/Else, Loops, and Functions

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Progress](https://img.shields.io/badge/Progress-Intermediate-yellow.svg)

## 📖 Description
This repository contains Python scripts and programs that demonstrate the use of if/else statements, loops, and functions. The goal is to provide a comprehensive understanding of control flow and function usage in Python. Each script is designed to be simple and easy to understand, making them ideal for learners who are looking to deepen their knowledge of Python control structures and functions.

The scripts cover a range of topics, including:
- If/else statements
- While and for loops
- Function definitions and calls
- Variable scope
- Lambda functions

## 📂 Contents
- **0-positive_or_negative.py**: Prints whether a number is positive, negative, or zero.
- **1-last_digit.py**: Prints the last digit of a number.
- **2-print_alphabet.py**: Prints the alphabet in lowercase.
- **3-print_alphabt.py**: Prints the alphabet in lowercase, except 'q' and 'e'.
- **4-print_hexa.py**: Prints numbers from 0 to 98 in decimal and hexadecimal.
- **5-print_comb2.py**: Prints numbers from 0 to 99.
- **6-print_comb3.py**: Prints all possible different combinations of two digits.
- **7-islower.py**: Checks for lowercase character.
- **8-uppercase.py**: Prints a string in uppercase.
- **9-print_last_digit.py**: Prints the last digit of a number.
- **10-add.py**: Adds two integers and returns the result.
- **11-pow.py**: Computes a to the power of b and returns the value.
- **12-fizzbuzz.py**: Prints the numbers from 1 to 100 with FizzBuzz logic.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-if_else_loops_functions
   ```
3. Run each script:
   ```bash
   python3 0-positive_or_negative.py
   ```

## 🛠️ Requirements
• Python 3.8+  
• Linux or macOS environment (recommended)

## Examples

### 0-positive_or_negative.py
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

### 1-last_digit.py
Prints the last digit of a number:
```python
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
print(f"Last digit of {number} is {last_digit} and is ", end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
```

### 2-print_alphabet.py
Prints the alphabet in lowercase:
```python
for letter in range(97, 123):
    print(chr(letter), end="")
print()
```

### 3-print_alphabt.py
Prints the alphabet in lowercase, except 'q' and 'e':
```python
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        print(chr(letter), end="")
print()
```

### 4-print_hexa.py
Prints numbers from 0 to 98 in decimal and hexadecimal:
```python
for number in range(99):
    print(f"{number} = {hex(number)}")
```

### 5-print_comb2.py
Prints numbers from 0 to 99:
```python
for number in range(100):
    if number != 99:
        print(f"{number:02d}, ", end="")
    else:
        print(f"{number:02d}")
```

### 6-print_comb3.py
Prints all possible different combinations of two digits:
```python
for i in range(10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print(f"{i}{j}, ", end="")
        else:
            print(f"{i}{j}")
```

### 7-islower.py
Checks for lowercase character:
```python
def islower(c):
    return ord(c) >= 97 and ord(c) <= 122

print(islower('a'))  # True
print(islower('A'))  # False
```

### 8-uppercase.py
Prints a string in uppercase:
```python
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print(char, end="")
    print()

uppercase("hello")
# Output: HELLO
```

### 9-print_last_digit.py
Prints the last digit of a number:
```python
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

print_last_digit(1234)
# Output: 4
```

### 10-add.py
Adds two integers and returns the result:
```python
def add(a, b):
    return a + b

print(add(1, 2))
# Output: 3
```

### 11-pow.py
Computes a to the power of b and returns the value:
```python
def pow(a, b):
    return a ** b

print(pow(2, 3))
# Output: 8
```

### 12-fizzbuzz.py
Prints the numbers from 1 to 100 with FizzBuzz logic:
```python
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

fizzbuzz()
# Output: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)