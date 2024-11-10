#!/usr/bin/python3
"""
Module to retrieve the dictionary representation of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object.

    Args:
        obj: The object to be converted.
    """
    return obj.__dict__
