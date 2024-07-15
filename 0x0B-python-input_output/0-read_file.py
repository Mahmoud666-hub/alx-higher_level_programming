#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    # with open(filename, "r", encoding='utf-8') as f: شغال برده
    """doc"""
    with open(filename, "r") as f:
        data = f.read()

    print(data, end="")
