#!/usr/bin/python3
"""The script deletes all State objects with a name
    containing the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    # Create a connection engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to check for all State objects with a name containing the letter 'a'
    states_to_del = session.query(State).filter(State.name.like('%a%')).all()

    # Check if any states were found
    if states_to_del:
        # Delete each state
        for state in states_to_del:
            session.delete(state)
        session.commit()
        print("Deleted all states with name containing 'a'.")
    else:
        print("No states with name containing 'a' found.")

    session.close()
