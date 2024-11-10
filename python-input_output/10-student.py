#!/usr/bin/python3
"""Module that defines a Student class."""

class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance with given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns selected attributes as a dictionary if `attrs` is given."""
        return {k: self.__dict__[k] for k in (attrs or self.__dict__)}
