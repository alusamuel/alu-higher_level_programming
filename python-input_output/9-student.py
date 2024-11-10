#!/usr/bin/python3
"""
Module with a Student class and a method to return its dictionary.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of the student.
        """
        return self.__dict__
