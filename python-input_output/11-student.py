#!/usr/bin/python3
""" Module that make student class """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}

    def reload_from_json(self, json):
        """Reloads attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
