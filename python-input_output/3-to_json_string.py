#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
