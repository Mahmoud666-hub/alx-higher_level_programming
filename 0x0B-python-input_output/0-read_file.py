#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename, "r", encoding='utf-8') as f:
        data = f.read()

    print(data)
