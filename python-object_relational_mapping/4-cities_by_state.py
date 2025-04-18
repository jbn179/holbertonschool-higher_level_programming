#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute SELECT query with JOIN
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
    """
    cursor.execute(query)

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
