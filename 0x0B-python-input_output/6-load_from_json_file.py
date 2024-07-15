#!/usr/bin/python3
"""json"""
import json


def load_from_json_file(filename):
    """fun"""
    with open(filename, "r") as f:
        n = json.loads(f.read())
    return n
