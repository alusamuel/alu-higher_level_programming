#!/usr/bin/python3


class Square:
    """A class that defines a square by its size, with validation, getters and setters, and an area method."""

    def __init__(self, size=0):
        """Initialize the square with a private instance attribute `size`."""
        self.size = size  # This uses the setter for validation.

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation.

        Args:
            value (int): The size of the square's side.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
