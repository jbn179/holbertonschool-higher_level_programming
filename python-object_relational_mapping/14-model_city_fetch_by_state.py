#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database),
        pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and their states
    results = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    # Print results
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
