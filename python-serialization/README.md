# Python Serialization 💾

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![JSON](https://img.shields.io/badge/JSON-Data-green.svg)
![Pickle](https://img.shields.io/badge/Pickle-Serialization-orange.svg)
![CSV](https://img.shields.io/badge/CSV-Data-yellow.svg)
![XML](https://img.shields.io/badge/XML-Markup-red.svg)

## 📖 Description
This project explores different methods of serialization and deserialization in Python. Serialization is the process of converting complex data structures into a format that can be easily stored or transmitted, while deserialization is the reverse process. The project demonstrates how to serialize Python objects in different formats (JSON, Pickle, CSV, XML) and how to deserialize these formats back into Python objects.

## 📂 Content
- **task_00_basic_serialization.py**: Implements basic serialization and deserialization using JSON
- **task_01_pickle.py**: Uses the pickle module to serialize and deserialize complex Python objects
- **task_02_csv.py**: Demonstrates how to work with tabular data in CSV format
- **task_03_xml.py**: Shows how to parse and generate data in XML format

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-serialization
   ```

3. Run the scripts:
   ```bash
   python3 task_00_basic_serialization.py
   ```

## 🛠️ Prerequisites
- Python 3.8+
- Ubuntu 20.04 LTS
- PEP 8 style compliance
- Complete documentation for all modules, classes, and functions

## Key Concepts ✨
- **Serialization**: Converting Python data structures into storable/transmissible formats
- **Deserialization**: Reconstructing Python objects from serialized data
- **JSON**: Language-independent data exchange format
- **Pickle**: Python-specific binary serialization protocol
- **CSV**: Simple tabular data format for data exchange
- **XML**: Extensible markup language for structuring hierarchical data
- **Data Persistence**: Maintaining object states between different program executions

## Examples

### JSON Serialization
```python
#!/usr/bin/python3
"""JSON Serialization Example"""
import json

# Create a Python dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "C"]
}

# Serialize to JSON string
json_string = json.dumps(data, indent=4)
print(json_string)

# Save to a file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### Pickle Serialization
```python
#!/usr/bin/python3
"""Pickle Serialization Example"""
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

# Create an object
person = Person("Alice", 25)

# Serialize with pickle
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

# Deserialize
with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)
    
print(loaded_person)  # Output: Alice (25)
```

### CSV Manipulation
```python
#!/usr/bin/python3
"""CSV Manipulation Example"""
import csv

# Write data to a CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "Paris"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "New York"]
]

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read data from a CSV file
with open("users.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(", ".join(row))
```

### XML Manipulation
```python
#!/usr/bin/python3
"""XML Manipulation Example"""
import xml.etree.ElementTree as ET

# Create an XML tree
root = ET.Element("users")

user1 = ET.SubElement(root, "user")
ET.SubElement(user1, "name").text = "Alice"
ET.SubElement(user1, "age").text = "25"
ET.SubElement(user1, "city").text = "Paris"

user2 = ET.SubElement(root, "user")
ET.SubElement(user2, "name").text = "Bob"
ET.SubElement(user2, "age").text = "30"
ET.SubElement(user2, "city").text = "London"

# Write the XML tree to a file
tree = ET.ElementTree(root)
tree.write("users.xml")

# Read an XML file
tree = ET.parse("users.xml")
root = tree.getroot()

for user in root.findall("user"):
    name = user.find("name").text
    age = user.find("age").text
    city = user.find("city").text
    print(f"{name} ({age}) from {city}")
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is licensed under the MIT License.

## Author ✍️
- Benjamin Ristord