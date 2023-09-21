#!/usr/bin/python3
'''creates a city and a state and their relationship'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
