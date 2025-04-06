# SQL More Queries 🔍

![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-blue.svg)
![Database](https://img.shields.io/badge/Database-Advanced-orange.svg)

## 📖 Description
This project builds upon the SQL basics and explores advanced query operations in MySQL. It focuses on user privileges, constraints, joins, unions, and subqueries. The scripts demonstrate how to manage user permissions, implement various types of table constraints, and write complex queries to extract specific data from multiple tables.

## 📂 Contents
- **0-privileges.sql**: Lists privileges of MySQL users
- **1-create_user.sql**: Creates a new MySQL user with all privileges
- **2-create_read_user.sql**: Creates a database and user with SELECT privilege only
- **3-force_name.sql**: Creates a table with a NOT NULL constraint
- **4-never_empty.sql**: Creates a table with a DEFAULT constraint
- **5-unique_id.sql**: Creates a table with a UNIQUE constraint
- **6-states.sql**: Creates a database and table with a PRIMARY KEY
- **7-cities.sql**: Creates a table with a FOREIGN KEY constraint
- **8-cities_of_california_subquery.sql**: Uses a subquery to filter results
- **9-cities_by_state_join.sql**: Performs an INNER JOIN between tables
- **10-genre_id_by_show.sql**: Lists shows with at least one linked genre
- **11-genre_id_all_shows.sql**: Lists all shows with their genre IDs (including NULL)
- **12-no_genre.sql**: Lists shows without a linked genre
- **13-count_shows_by_genre.sql**: Counts shows by genre
- **14-my_genres.sql**: Lists genres of a specific show
- **15-comedy_only.sql**: Lists all comedy shows
- **16-shows_by_genre.sql**: Lists all shows and their linked genres

## 🚀 Getting Started
1. Install MySQL 8.0 on Ubuntu 20.04:
   ```bash
   sudo apt update
   sudo apt install mysql-server
   ```

2. Start the MySQL service:
   ```bash
   sudo service mysql start
   ```

3. Connect to MySQL and run the SQL scripts:
   ```bash
   mysql -hlocalhost -uroot -p < 0-privileges.sql
   ```

## 🛠️ Requirements
- MySQL 8.0 or higher
- Ubuntu 20.04 LTS
- All SQL queries should be properly commented
- All files should end with a new line

## Key Concepts ✨
- **User Management**: Creating users and granting privileges
- **Constraints**: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, DEFAULT
- **Joins**: INNER JOIN, LEFT JOIN, RIGHT JOIN
- **Subqueries**: Queries nested within other queries
- **Relationships**: One-to-one, One-to-many, Many-to-many
- **Aggregation**: GROUP BY, COUNT, AVG and other aggregate functions

## Examples

### Creating a User with Privileges
```sql
-- Creates a user and grants all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### Creating a Table with Constraints
```sql
-- Creates a table with PRIMARY KEY and FOREIGN KEY constraints
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
```

### Using Joins
```sql
-- Lists all cities with their state names using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
```

### Subqueries
```sql
-- Lists all cities of California using a subquery
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author ✍️
- Benjamin Ristord