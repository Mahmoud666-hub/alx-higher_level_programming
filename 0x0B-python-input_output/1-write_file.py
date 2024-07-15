#!/usr/bin/python3
"""python"""


def write_file(filename="", text=""):
    """fun"""
    with open(filename, "w", encoding="UTF8") as f:
        num_chr = f.write(text)
    return num_chr
