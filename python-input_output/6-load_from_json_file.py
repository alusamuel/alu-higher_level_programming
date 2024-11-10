#!/usr/bin/python3
"""
Module to load a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read the JSON string from.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
