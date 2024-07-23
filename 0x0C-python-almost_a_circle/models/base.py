#!/usr/bin/python3
"""new"""


class Base:
    """class"""
    __nb_objects = 0
    """attr class"""
    def __init__(self, id=None):
        """cons"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
