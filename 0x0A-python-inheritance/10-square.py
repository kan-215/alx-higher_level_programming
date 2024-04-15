#!/usr/bin/python3
"""Module 9-rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Return the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return Rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return Square description"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
