#!/usr/bin/python3
"""
Module to convert a JSON string back into a Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted.
    """
    return json.loads(my_str)
