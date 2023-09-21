#!/usr/bin/python3
'''
prints the city objects from the database hbtn_0e_6_usa
script takes 3 arguments
'''

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


def main():
    """
    this function prints the city objects
    from the hbtn_0e_6_usa database
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id.asc()).all()
    session.close()
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    main()
