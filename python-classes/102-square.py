#!/usr/bin/python3
"""Square class definition."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Get the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size, must be a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is smaller than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is smaller or equal to another based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is larger than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is larger or equal to another based on area."""
        return self.area() >= other.area()

