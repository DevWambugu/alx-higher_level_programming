#!/usr/bin/python3
'''
prints all State objects
ID
script takes 4 arguments
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    this function prints state objects ID
    from the hbtn_0e_6_usa database
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (session.query(State).filter(State.name == state_name).first())
    session.close()
    if not state:
        print("Not found")
    else:
        print(state.id)


if __name__ == "__main__":
    main()
