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

    def to_json(self, attrs=None):
        '''This function retrieves a dictionary
        representation of a Student instance'''
        if attrs is None:
            return self.__dict__
        else:
            if all(isinstance(attr, str) for attr in attrs):
                return {attr: getattr(self, attr)
                        for attr in attrs if hasattr(self, attr)}
            else:
                return self.__dict__

    def reload_from_json(self, json):
        '''This function/ method
        replaces all attributes of the Student instance'''
        for i, j in json.items():
            setattr(self, i, j)
