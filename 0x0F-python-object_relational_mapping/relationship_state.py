#!/usr/bin/python3
'''
contains the class definition of a State
and an instance Base = declarative_base()
'''

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''inherits from Base Tips and
    links to the MySQL table states
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
