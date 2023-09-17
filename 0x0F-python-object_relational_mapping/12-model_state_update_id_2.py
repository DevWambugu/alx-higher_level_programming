#!/usr/bin/python3
'''
changes a state at a given ID
script takes 3 arguments
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    this function updates a state on a given id
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = 'New Mexico'
    state_to_update = session.query(State).filter_by(id=2).first()
    state_to_update.name = new_state
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
