#!/usr/bin/python3
"""This is append file function"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
