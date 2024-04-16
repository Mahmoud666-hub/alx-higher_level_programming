#!/usr/bin/python3
class MyList(list):
    def __init__(self):
        return super().__init__()

    def print_sorted(self):
        print(sorted(self))
