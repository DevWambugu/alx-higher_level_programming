#!/usr/bin/python3
# 4-inherits_from.py
# DevWambugu
"""checks if bject is an instance of a class that inherited
   (directly or indirectly) from the specified class."""


   def inherits_from(obj, a_class):
       '''this function returns True if the object is an instance of a
       class that inherited (directly or indirectly) 
       from the specified class ; otherwise False
       '''
       return isinstance(obj, a_class) and type(obj) != a_class
