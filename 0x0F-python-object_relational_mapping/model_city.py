#!/usr/bin/python3
'''
contains the class definition of a city
and an instance Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    '''inherits from class State and
    links to the MySQL table citiess
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
