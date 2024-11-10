#!/usr/bin/python3
"""This is readfile"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
