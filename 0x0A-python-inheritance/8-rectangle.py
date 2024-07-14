#!/usr/bin/python3
"""module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""rect"""


class Rectangle(BaseGeometry):
    """rect"""
    def __init__(self, width, height):
        self.__width = BaseGeometry.integer_validator("width", width)
        self.__height = BaseGeometry.integer_validator("height", height)
