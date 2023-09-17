#!/usr/bin/python3
'''
adds a state name and prints it
script takes 3 arguments
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    this function prints state objects
    from the hbtn_0e_6_usa database
    after addition of state object
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == "__main__":
    main()
