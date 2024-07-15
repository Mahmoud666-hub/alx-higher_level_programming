#!/usr/bin/python3
"""new"""


def append_write(filename="", text=""):
    """fun"""
    with open(filename, "a", encoding="UTF8") as f:
        num = f.write(text)
    return num
