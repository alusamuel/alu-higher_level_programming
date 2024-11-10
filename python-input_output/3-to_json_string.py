#!/usr/bin/python3
"""Module to convert a Python object to a JSON string."""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: The Python object to be converted.
    """
    return json.dumps(my_obj)
