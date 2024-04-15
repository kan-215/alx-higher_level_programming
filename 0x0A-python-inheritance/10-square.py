#!/usr/bin/python3
"""Module 9-rectangle"""


from typing import Union


class BaseGeometry:
    """BaseGeometry class"""

    def area(self) -> None:
        """Placeholder for area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: Union[int, float]) -> None:
        """Validate value as integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width: int, height: int) -> None:
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self) -> int:
        """Return the area ofthe  Rectangle"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class"""

    def __init__(self, size: int) -> None:
        """Initialize the  Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self) -> int:
        """Return the area of the  Square"""
        return self.__size ** 2
