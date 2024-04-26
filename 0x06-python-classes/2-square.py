#!/usr/bin/python3
'''class'''


class Square:
    '''square class'''
    def __init__(self, size=0):
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
