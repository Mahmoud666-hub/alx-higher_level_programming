#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
words = str.split(); str = " ".join([words[5], words[6], words[12], words[0]])
print(str)
  # str = " ".join([1st, 2nd, 3rd]) important