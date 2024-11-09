#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square by its size, with validation and an area method."""

    def __init__(self, size=0):
        """Initialize the square with a private instance attribute `size`.

        Args:
            size (int): The size of the square's side, default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
