#!/usr/bin/python3
"""_summary_

Raises:
    TypeError: not correct data type
    ValueError: _description_
    TypeError: _description_
    ValueError: _description_

Returns:
    _type_: _description_
"""


class Square:
    """Represent a square."""
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
        """Return the current area of the square."""
        return (self.__size * self.__size)

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
