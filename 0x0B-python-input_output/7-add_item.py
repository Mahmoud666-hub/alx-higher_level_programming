#!/usr/bin/python3
"""json"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile("add_item.json"):
    ls = load_from_json_file("add_item.json")
else:
    ls = []
ls.extend(sys.argv[1:]) #extend(بيكمل  داخل نفس العنصر) append(بتضيف جواها عنصر جديد)
save_to_json_file(ls, "add_item.json")
