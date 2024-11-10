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
        """
        Returns a dictionary of the instance's attributes.
        If `attrs` is provided as a list, only returns those attributes.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
