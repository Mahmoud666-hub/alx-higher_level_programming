#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    x = 0
    for i, m in a_dictionary.items():
        if x < m:
            x = m
            y = i
    return y
