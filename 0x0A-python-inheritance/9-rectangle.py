#!/usr/bin/python3
"""module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""rect"""


class Rectangle(BaseGeometry):
    """rect"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


# r = Rectangle(4, 5)
# print(r)
# print(r.area())
