#!/usr/bin/python3
"""
This module defines a Square class that represents a square object.

Raises:
    TypeError: If the size provided is not an integer.
    ValueError: If the size provided is less than zero.

Returns:
    int: The area of the square.
"""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with '#' characters."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
