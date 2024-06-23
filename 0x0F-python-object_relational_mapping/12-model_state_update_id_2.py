#!/usr/bin/python3
"""The script changes the name of a State object from the database hbtn_0e_6_usa"""

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

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to check for the State object where id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the state exists
    if state_to_update:
        # Change the name of the state to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()
        print("State name updated successfully.")
    else:
        print("State with ID 2 not found.")

    # Close the session
    session.close()
