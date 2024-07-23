#!/usr/bin/python3
"""
rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class:
    inherits from Base
    attr:
    width of rect
    height of rect
    x
    y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ constructor
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        retangle height
        """
        return self.__width

    @property
    def height(self):
        """
        retangle height
        """
        return self.__height

    @property
    def x(self):
        """
        retangle height
        """
        return self.__x

    @property
    def y(self):
        """
        retangle height
        """
        return self.__y

    @width.setter
    def width(self, val):
        """
        retangle height
        """
        self.__width = val

    @height.setter
    def height(self, val):
        """
        retangle height
        """
        self.__height = val

    @x.setter
    def x(self, x):
        """
        retangle height
        """
        self.__x = x

    @y.setter
    def y(self, val):
        """
        retangle height
        """
        self.__y = val
