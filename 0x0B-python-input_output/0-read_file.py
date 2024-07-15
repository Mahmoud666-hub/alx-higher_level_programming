#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename, "r") as f:
        data = f.read(-1)

    if data != "":
        print(data)
