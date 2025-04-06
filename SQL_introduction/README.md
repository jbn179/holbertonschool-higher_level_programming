# SQL Introduction 🗃️

![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-blue.svg)
![Database](https://img.shields.io/badge/Database-Fundamentals-orange.svg)

## 📖 Description
This project provides an introduction to SQL (Structured Query Language) and MySQL database management. It covers fundamental database concepts and SQL commands to create, manipulate, and query databases. The scripts and commands in this project demonstrate how to work with MySQL servers, create and modify databases, tables, and perform various operations on data.

## 📂 Contents
- **0-list_databases.sql**: Shows all databases on a MySQL server
- **1-create_database_if_missing.sql**: Creates a database if it doesn't exist
- **2-remove_database.sql**: Deletes a database if it exists
- **3-list_tables.sql**: Lists all tables in a specified database
- **4-first_table.sql**: Creates a table in the current database
- **5-full_table.sql**: Prints the full description of a table
- **6-list_values.sql**: Lists all rows of a table
- **7-insert_value.sql**: Inserts a new row into a table
- **8-count_89.sql**: Displays the number of records with specific value
- **9-full_creation.sql**: Creates a table and adds multiple rows
- **10-top_score.sql**: Lists all records of a table ordered by score
- **11-best_score.sql**: Lists records with score >= 10
- **12-no_cheating.sql**: Updates a score in a table
- **13-change_class.sql**: Removes records with score <= 5
- **14-average.sql**: Computes the average score of all records
- **15-groups.sql**: Lists number of records with same score
- **16-no_link.sql**: Lists all records with a name value

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
   mysql -hlocalhost -uroot -p < 0-list_databases.sql
   ```

## 🛠️ Requirements
- MySQL 8.0 or higher
- Ubuntu 20.04 LTS
- All SQL queries should be properly commented
- All files should end with a new line

## Key Concepts ✨
- **Database**: A structured set of data
- **SQL**: Language used to communicate with relational databases
- **MySQL**: Popular open-source database management system
- **DDL (Data Definition Language)**: Commands like CREATE, ALTER, DROP
- **DML (Data Manipulation Language)**: Commands like SELECT, INSERT, UPDATE, DELETE
- **Queries**: Instructions to retrieve data from a database

## Examples

### Creating a Database
```sql
-- Creates a database named hbtn_0c_0 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

### Creating a Table
```sql
-- Creates a table named first_table with id and name columns
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```

### Inserting Data
```sql
-- Inserts a new row into first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

### Selecting Data
```sql
-- Lists all records with score >= 10 in second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author ✍️
- Benjamin Ristord