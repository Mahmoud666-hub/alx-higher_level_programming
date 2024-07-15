#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename, "rb") as f:
        data = f.read()

    if data !="":
        print(data)
