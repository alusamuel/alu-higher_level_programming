#!/usr/bin/python3
""" Module that make student class """


class Student:
    def __init__(self, first_name, last_name, age):
       """Initializes a student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the student's attributes as a dictionary."""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
