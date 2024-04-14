#!/usr/bin/python3
import os
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    i = 0
    while i < len(name):
        if name[i][:2] != "__":
            print("{}".format(name[i]))
        i += 1
