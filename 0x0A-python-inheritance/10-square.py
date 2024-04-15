#!/usr/bin/python3
"""Module implementing Rectangle and Square classes"""

from typing import Union

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width: int, height: int) -> None:
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self) -> int:
        """Return the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return Rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class"""

    def __init__(self, size: int) -> None:
        """Initialize Square"""
        super().__init__(size, size)

    def __str__(self) -> str:
        """Return Square description"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
