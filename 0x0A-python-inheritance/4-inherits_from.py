#!/usr/bin/python3
"""ygygy"""


def inherits_from(obj, a_class):
    """lll"""
    return issubclass(type(obj), a_class) or isinstance(obj, a_class)

# print(issubclass(type(True), object))
