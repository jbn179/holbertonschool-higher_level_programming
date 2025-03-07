#!/usr/bin/python3
"""Script that displays states where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

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

    # Execute SELECT query with LIKE filter
    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id
    """.format(state)

    cursor.execute(query)

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
