#!/usr/bin/python3
"""Module implementing Square and Rectangle classes"""


from typing import Union


class BaseGeometry:
    """BaseGeometry class for geometric operations"""

    def area(self) -> None:
        """Placeholder for area method"""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name: str, value: Union[int, float]) -> None:
        """Validates if value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class representing a rectangle"""

    def __init__(self, width: int, height: int) -> None:
        """Initialize Rectangle instance with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self) -> int:
        """Compute and return the area of the rectangle"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class representing a square, inherits from Rectangle"""

    def __init__(self, size: int) -> None:
        """Initialize Square instance with size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self) -> int:
        """Compute and return the area of the square"""
        return self.__size ** 2
