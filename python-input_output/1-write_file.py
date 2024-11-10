#!/usr/bin/python3
"""This module contains a function to write text to a file."""


def write_file(filename="", text=""):
    """
    Writes text to a file.

    Args:
        filename (str): The file to write to (default is an empty string).
        text (str): The text to write.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
