#!/usr/bin/python3


"""new one"""


def is_same_class(obj, a_class):
    """function"""
    if a_class != object:
        return isinstance(obj, a_class)
    return False
