#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print(f"{chr(i)}", end="")
    else:
        continue
