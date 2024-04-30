#!/usr/bin/python3
'''print'''


def text_indentation(text):
    '''print'''
    # a = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # for i in text:
    #     a += 1
    #     if i in ['.', '?', ':']:
    #         print("{}".format(i), end="\n\n")
    #     else:
    #         if (text[a - 2] in ['.', '?', ':', '\n']) and i == ' ':
    #             continue
    #         else:
    #             print("{}".format(i), end="")
    for i in ['.', '?', ':']:
        text = (i + "\n\n").join(
            [line.strip(" ") for line in text.split(i)])

    print("{}".format(text), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
# text_indentation("Holberton. School? How are you: John")
