#!/usr/bin/python3
"""MagicClass representing a circle."""

import math


class MagicClass:
    """A class for a circle."""

    def __init__(self, radius=0):
        """Initialize the circle with a given radius."""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return (2 * math.pi * self.__radius)
