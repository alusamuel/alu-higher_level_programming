#!/usr/bin/python3
"""This module contains a function to read and print a file."""


def read_file(filename=""):
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The file to read (default is an empty string).
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
