#!/usr/bin/python3
"""Script that safely displays states where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute SELECT query with parameterized query
    query = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY states.id
        """
    cursor.execute(query, (state_name,))

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
