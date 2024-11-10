#!/usr/bin/python3
"""
Module to save a Python object as a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file as a JSON string.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The name of the file where the object will be saved.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
