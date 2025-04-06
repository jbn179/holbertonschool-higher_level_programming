# 📚 Holberton School Higher Level Programming

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange.svg)
![Progress](https://img.shields.io/badge/Progress-Advanced-green.svg)

## 📖 Description
This repository contains a collection of projects developed as part of the Holberton School Higher Level Programming curriculum. The projects cover various programming languages and concepts with a primary focus on Python, along with JavaScript, SQL, and web development. Each directory represents a specific topic or project designed to build and enhance programming skills from foundational to advanced levels.

The projects cover a range of topics, including:
- Python fundamentals and advanced concepts
- Object-oriented programming
- Data structures and algorithms
- Database manipulation with SQL
- Web front-end with JavaScript
- REST API development
- Object-relational mapping
- Test-driven development

## 📂 Contents

### Python Projects
- **python-hello_world**: Introduction to Python programming basics.
- **python-if_else_loops_functions**: Control flow, loops, and function definitions.
- **python-import_modules**: Importing and utilizing modules in Python.
- **python-data_structures**: Lists, tuples, and basic data structures.
- **python-more_data_structures**: Dictionaries, sets, and functional programming concepts.
- **python-exceptions**: Error handling and exception management.
- **python-classes**: Object-oriented programming in Python.
- **python-more_classes**: Advanced OOP concepts and class implementations.
- **python-test_driven_development**: Writing and running tests in Python.
- **python-inheritance**: Class inheritance and object hierarchies.
- **python-input_output**: File handling, JSON serialization, and deserialization.
- **python-serialization**: Converting objects to different formats (JSON, Pickle, CSV, XML).
- **python-object_relational_mapping**: Using SQLAlchemy to map Python classes to database tables.
- **python-server_side_rendering**: Server-side template rendering techniques.

### Web Development
- **javascript-dom_manipulation**: JavaScript DOM manipulation and web interactivity.
- **restful-api**: Building and consuming RESTful APIs.

### Database Projects
- **SQL_introduction**: Introduction to SQL and database concepts.
- **SQL_more_queries**: Advanced SQL queries, joins, and database management.

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/jbn179/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the desired project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-hello_world
   ```
3. Run the scripts according to the project's requirements:
   ```bash
   python3 2-print.py
   ```

## 🛠️ Requirements
- Python 3.8+
- MySQL 8.0+ (for SQL projects)
- Node.js (for JavaScript projects)
- Ubuntu 20.04 LTS (recommended)

## Examples

### Python Classes
```python
#!/usr/bin/python3
"""Define a class Square"""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
```

### JavaScript DOM Manipulation
```javascript
// Select an HTML element and modify its content
document.getElementById('header').textContent = 'New Header Text';

// Add event listeners to elements
document.querySelector('button').addEventListener('click', function() {
    alert('Button was clicked!');
});
```

### SQL Query
```sql
-- Select data with multiple joins
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
```

### Python Object-Relational Mapping
```python
#!/usr/bin/python3
"""Lists all State objects from the database"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author
Benjamin Ristord - [@jbn179](https://github.com/jbn179)