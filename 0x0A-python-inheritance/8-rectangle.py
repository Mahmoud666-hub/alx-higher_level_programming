#!/usr/bin/python3
"""module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""rect"""


class Rectangle(BaseGeometry):
    """rect"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
