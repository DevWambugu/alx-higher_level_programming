#!/usr/bin/python3
'''
This scriptlists all State objects
from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    '''
    Get all state objects from the database
    '''

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(f"{state.id}:", state.name)
    session.close()


if __name__ == "__main__":
    main()
