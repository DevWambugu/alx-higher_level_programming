#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
script takes 3 arguments
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def first_state_object():
    """
    this function prints the first state object
    from the hbtn_0e_6_usa database
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    session.close()
    if state is None:
        print('Nothing')
    else:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    first_state_object()
