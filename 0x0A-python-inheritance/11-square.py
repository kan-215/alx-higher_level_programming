#!/usr/bin/python3
"""python module 9-rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initializes Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Return the  Square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
