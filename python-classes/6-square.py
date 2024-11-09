#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square by its size and position, with validation, getters and setters, area, and print functionality."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position, using setters for validation."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute with validation.

        Args:
            value (tuple): The position of the square, represented as (x, y) coordinates.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' according to its position.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print new lines for vertical position (position[1])
        print("\n" * self.__position[1], end="")

        # Print the square with spaces for horizontal position (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
