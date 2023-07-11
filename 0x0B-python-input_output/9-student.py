#!/usr/bin/python3
#  9-student.py
#  DevWambugu
'''a class that defines the class student with public attributes'''


class Student:
    '''This class defines the class student'''
    def __init__(self, first_name, last_name, age):
        '''initializes the public attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''This function retrieves a dictionary
        representation of a Student instance'''
        return self.__dict__
