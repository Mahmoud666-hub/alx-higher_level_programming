#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    if number % 10 == 0:
        print(f"Last digit of {number} is {number%10} and is 0")
    elif number % 10 > 5:
        print(f"Last digit of {number} is {number%10} and is greater than 5")
    else:
        t = number % 10
        print(f"Last digit of {number} is {t} and is less than 6 and not 0")
else:
    new = number
    number = number * (-1)
    print(f"Last digit of {new} is -{number%10} and is less than 6 and not 0")
