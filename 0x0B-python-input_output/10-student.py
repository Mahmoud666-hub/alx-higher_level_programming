#!/usr/bin/python3
"""new"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        r = {}
        if attrs is not None and isinstance(attrs, list) and \
                all(isinstance(x, str) for x in attrs):
            for a in attrs:
                if a in self.__dict__:
                    r.update({a: self.__dict__[a]})
            return r
        else:
            return self.__dict__
# s= Student("da", "as", 32)
# print(s.to_json())
