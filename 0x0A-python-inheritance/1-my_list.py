#!/usr/bin/python3
""" class inheritance """


class MyList(list):
    """ initiation """
    def __init__(self):
        return super().__init__()

    """ print sorted """

    def print_sorted(self):
        print(sorted(self))
