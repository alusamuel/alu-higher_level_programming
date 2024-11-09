#!/usr/bin/python3
"""Square class definition."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the square's position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, must be a tuple of two non-negative integers."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        result = []
        for i in range(self.__position[1]):
            result.append("")
        for i in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)

