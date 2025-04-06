# Python Object-Relational Mapping 🔄

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-red.svg)

## 📖 Description
This project bridges the gap between Python and databases using both direct MySQL connections and SQLAlchemy ORM (Object-Relational Mapping). It demonstrates how to query, create, modify, and delete data from a database using Python code instead of raw SQL. The project illustrates two approaches: using MySQLdb for direct database access and SQLAlchemy as an abstraction layer.

## 📂 Contents
- **0-select_states.py**: Lists all states from a database using MySQLdb
- **1-filter_states.py**: Lists states with names starting with 'N'
- **2-my_filter_states.py**: Searches for specific states based on user input
- **3-my_safe_filter_states.py**: SQL injection-safe state search
- **4-cities_by_state.py**: Lists all cities with their state names using JOIN
- **5-filter_cities.py**: Lists cities of a specific state
- **6-model_state.py**: Defines a State class using SQLAlchemy
- **7-model_state_fetch_all.py**: Lists all State objects using SQLAlchemy
- **8-model_state_fetch_first.py**: Prints the first State object
- **9-model_state_filter_a.py**: Lists states containing the letter 'a'
- **10-model_state_my_get.py**: Gets a state by name using SQLAlchemy
- **11-model_state_insert.py**: Adds a new state to the database
- **12-model_state_update_id_2.py**: Updates a state's name
- **13-model_state_delete_a.py**: Deletes states containing the letter 'a'
- **14-model_city_fetch_by_state.py**: Lists cities with their state names using SQLAlchemy
- **models/**: Directory containing SQLAlchemy model definitions

## 🚀 Getting Started
1. Install required packages:
   ```bash
   sudo apt-get install python3-dev libmysqlclient-dev
   pip3 install MySQLdb
   pip3 install SQLAlchemy
   ```

2. Set up your MySQL database:
   ```bash
   mysql -u root -p < setup_mysql_dev.sql
   ```

3. Run the scripts:
   ```bash
   python3 0-select_states.py root root hbtn_0e_0_usa
   ```

## 🛠️ Requirements
- Python 3.8+
- Ubuntu 20.04 LTS
- MySQL 8.0+
- MySQLdb 2.0.x
- SQLAlchemy 1.4+
- PEP 8 style compliance

## Key Concepts ✨
- **ORM**: Object-Relational Mapping - converting data between incompatible type systems
- **MySQLdb**: Python interface to MySQL database
- **SQLAlchemy**: SQL toolkit and ORM for Python
- **Declarative Base**: SQLAlchemy system for defining classes mapped to database tables
- **Session**: SQLAlchemy's way to communicate with the database
- **SQL Injection**: Security vulnerability and how to prevent it
- **Model Relationships**: Defining connections between tables

## Examples

### Direct MySQL Access with MySQLdb
```python
#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
```

### Using SQLAlchemy ORM
```python
#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    
    session.close()
```

### Defining a Model with SQLAlchemy
```python
#!/usr/bin/python3
"""Contains the State class definition"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class definition for State mapped to states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author ✍️
- Benjamin Ristord