#!/usr/bin/python3
"""
Rectangle Module

This module defines a Rectangle class with width and height attributes.

Raises:
    TypeError: If the width or height is not an integer.
    ValueError: If the width or height is less than or equal to 0.

Returns:
    A Rectangle object with specified width and height.
"""


class Rectangle:
    """A rectangle class with width and height attributes."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width attribute with type and value checks."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height attribute with type and value checks."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        self.__height = height
