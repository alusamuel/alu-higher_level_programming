#!/usr/bin/python3
"""This module contains a function to append text to a file."""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename (str): The file to append to (default is an empty string).
        text (str): The text to append.
    
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
