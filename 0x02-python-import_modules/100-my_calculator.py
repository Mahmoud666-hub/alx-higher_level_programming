#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        c = ["+", "-", "*", "/"]
        x = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
        i = 0
        while i < len(c):
            if argv[2] == c[i]:
                print("{0} {1} {2} = {3}".format(a, c[i], b, x[i]))
                break
            i += 1
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
