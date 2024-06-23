from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the Base instance
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Database connection settings
DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost:3306/your_database'

# Create the engine
engine = create_engine(DATABASE_URI, echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Example usage: adding a new state
new_state = State(name='California')
session.add(new_state)
session.commit()

# Query the database
for state in session.query(State).all():
    print(state.id, state.name)

# Close the session
session.close()
