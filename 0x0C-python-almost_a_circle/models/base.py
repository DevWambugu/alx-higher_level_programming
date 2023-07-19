#!/usr/bin/python3
#  base.py
#  DevWambugu
'''This class is be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
'''
import json
import csv


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation
        of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        name_of_file = cls.__name__ + ".json"
        with open(name_of_file, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dictionaries))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''This function serializes a csv file
        Format of the CSV:
        Rectangle: <id>,<width>,<height>,<x>,<y>
        Square: <id>,<size>,<x>,<y>'''
        name = cls.__name__ + ".csv"
        '''Write the csv file'''
        with open(name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def create(cls, **kwargs):
        """ This function Returns an
        instance with all attributes already set
        it will be used in the deserialization
	of a csv file"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**kwargs)
        return dummy

    @classmethod
    def load_from_file_csv(cls):
        '''This function deserializes a csv file. File Name and Field Names'''
        name = cls.__name__ + ".csv"
        try:
            '''read the csv file'''
            with open(name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=field_names)

                # Handle empty strings or set default values
                list_dicts = [
                    {key: int(value) if value.strip() != '' else 0 for key, value in d.items()}
                    for d in list_dicts
                ]
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
