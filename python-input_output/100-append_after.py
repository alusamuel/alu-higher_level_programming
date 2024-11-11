#!/usr/bin/python3
"""Module for inserting text after specific lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts `new_string` after each line in `filename`.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to look for in each line.
        new_string (str): The string to add after each matching line.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Read all lines

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
