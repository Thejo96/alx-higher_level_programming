#!/usr/bin/python3
"""Defines Base class"""
import json
import csv
import turtle


class Base:
    """Base class body.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Id in a constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            @staticmethod
            def to_json_string(list_dictionaries):
                """Convert list of dictionaries to a JSON string
                """
                if list_dictionaries is None or list_dictionaries == []:
                    return "[]"
                return json.dumps(list_dictionaries)

            # ... rest of your class methods ...


            if __name__ == "__main__":
                r1 = Rectangle(10, 7, 2, 8)
                dictionary = r1.to_dictionary()
                json_dictionary = Base.to_json_string([dictionary])
                print(dictionary)
                print(type(dictionary))
                print(json_dictionary)
                print(type(json_dictionary)
