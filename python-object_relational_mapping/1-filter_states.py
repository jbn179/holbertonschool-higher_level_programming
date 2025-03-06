#!/usr/bin/python3
"""Script that lists all states with names starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all 3 arguments are provided
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

    # Execute SELECT query with LIKE filter
    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY states.id
    """)

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
