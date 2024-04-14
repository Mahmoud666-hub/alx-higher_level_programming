#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{}".format(0))
    elif len(argv) == 2:
        print("{}".format(int(argv[1])))
    else:
        i = 1
        sum = 0
        while i < len(argv):
            sum += int(argv[i])
            i += 1
        print("{}".format(sum))
