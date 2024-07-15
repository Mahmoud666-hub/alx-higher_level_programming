#!/usr/bin/python3
"""json"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


with open("add_item.json", "a") as f:
    save_to_json_file(sys.argv[1:], "add_item.json")
