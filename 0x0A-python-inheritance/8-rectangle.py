#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""rect"""


class Rectangle(BaseGeometry):
    """rect"""
    def __init__(self, width, height):
        self.__width = Rectangle.integer_validator("width", width)
        self.__height = Rectangle.integer_validator("height", height)
