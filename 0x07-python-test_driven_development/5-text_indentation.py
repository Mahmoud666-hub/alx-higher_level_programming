#!/usr/bin/python3
'''print'''


def text_indentation(text):
    '''print'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            print("{}".format(i), end="")
            print("\n" * 2, end="")
        else:
            print("{}".format(i), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
