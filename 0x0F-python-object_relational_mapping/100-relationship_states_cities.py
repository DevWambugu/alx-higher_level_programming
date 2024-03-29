#!/usr/bin/python3
'''
creates a city and a state and their relationship
script takes 3 arguments
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City
from sys import argv


def main():
    """creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa"""

    password = argv[2]
    username = argv[1]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
