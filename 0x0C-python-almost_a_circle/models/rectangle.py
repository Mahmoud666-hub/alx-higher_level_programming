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
        width getter
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
    def width(self, Width):
        """
        widht setter
        """
        if type(Width) is not int:
            raise TypeError("width must be an integer")
        if Width <= 0:
            raise ValueError("width must be > 0")
        self.__width = Width

    @height.setter
    def height(self, val):
        """
        retangle height
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """
        retangle height
        """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        elif val <= 0:
            raise ValueError("x must be > 0")
        self.__x = val

    @y.setter
    def y(self, val):
        """
        retangle height
        """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        elif val <= 0:
            raise ValueError("y must be > 0")
        self.__y = val
