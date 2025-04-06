# Python Input/Output 📂

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![File IO](https://img.shields.io/badge/File-IO-green.svg)

## 📖 Description
This project explores file handling and input/output operations in Python. It covers reading from and writing to files, working with JSON for data serialization and deserialization, and handling both text and binary files. The exercises demonstrate various file operations, including opening, reading, writing, and appending to files using different methods and techniques.

## 📂 Contents
- **0-read_file.py**: Function that reads a text file and prints its contents to stdout
- **1-write_file.py**: Function that writes a string to a text file and returns the number of characters written
- **2-append_write.py**: Function that appends a string to the end of a text file
- **3-to_json_string.py**: Function that returns the JSON string representation of an object
- **4-from_json_string.py**: Function that returns an object represented by a JSON string
- **5-save_to_json_file.py**: Function that writes an object to a text file using JSON representation
- **6-load_from_json_file.py**: Function that creates an object from a JSON file
- **7-add_item.py**: Script that adds all command line arguments to a Python list and saves them to a file
- **8-class_to_json.py**: Function that returns the dictionary description for JSON serialization of an object
- **9-student.py**: Class Student that defines student attributes and converts to JSON
- **10-student.py**: Enhanced Student class with filtered attribute conversion
- **11-student.py**: Student class with methods to save and reload from JSON
- **12-pascal_triangle.py**: Function that returns a list of lists representing Pascal's triangle

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-input_output
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
- **File Operations**: Opening, reading, writing, and closing files
- **File Modes**: Different modes for opening files (`r`, `w`, `a`, `r+`, etc.)
- **Context Managers**: Using `with` statements for safe file handling
- **JSON**: JavaScript Object Notation for data serialization/deserialization
- **Serialization**: Converting objects to a storable or transmittable format
- **Deserialization**: Converting stored/transmitted data back to objects
- **Text vs Binary Files**: Understanding different file formats
- **Working with Paths**: Handling file paths across operating systems

## Examples

### Reading from a File
```python
#!/usr/bin/python3
"""Function to read and print a text file"""


def read_file(filename=""):
    """Read a text file (UTF8) and print its contents to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")


# Usage
read_file("my_file.txt")
```

### Writing to a File
```python
#!/usr/bin/python3
"""Function to write to a text file"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)


# Usage
nb_characters = write_file("my_file.txt", "This is a test string.\n")
print(nb_characters)  # 23
```

### Working with JSON
```python
#!/usr/bin/python3
"""Functions for JSON serialization and deserialization"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# Usage
my_list = [1, 2, 3]
save_to_json_file(my_list, "list.json")
new_list = load_from_json_file("list.json")
print(new_list)  # [1, 2, 3]
```

### Class to JSON Conversion
```python
#!/usr/bin/python3
"""Class with JSON serialization capabilities"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary of Student instance with specified attributes"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}


# Usage
student = Student("John", "Doe", 23)
json_student = student.to_json()
print(json_student)  # {'first_name': 'John', 'last_name': 'Doe', 'age': 23}
json_student_attrs = student.to_json(['first_name', 'age'])
print(json_student_attrs)  # {'first_name': 'John', 'age': 23}
```

### Pascal's Triangle
```python
#!/usr/bin/python3
"""Pascal's Triangle implementation"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n"""
    if n <= 0:
        return []
        
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


# Usage
for row in pascal_triangle(5):
    print(row)
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author ✍️
- Benjamin Ristord