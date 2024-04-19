#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    x = 0
    for i, m in a_dictionary.items():
        if x < m:
            x = m
            y = i
    return y
