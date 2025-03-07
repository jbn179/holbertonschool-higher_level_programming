#!/usr/bin/python3
"""Script that lists all cities of a state from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments
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

    # Execute SELECT query with JOIN and safe parameter binding
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
    """
    cursor.execute(query, (state_name,))

    # Fetch results and format output
    results = cursor.fetchall()
    print(", ".join([row[0] for row in results]))

    # Close cursor and database connection
    cursor.close()
    db.close()
