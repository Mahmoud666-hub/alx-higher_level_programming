#!/usr/bin/python3
# from base import Base
Base = __import__('base').Base
"""module"""


class Rectangle(Base):
    """new class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        (super).__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, val):
        self.__width = val

    @height.setter
    def height(self, val):
        self.__height = val

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, val):
        self.__y = val
