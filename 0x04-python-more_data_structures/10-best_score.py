#!/usr/bin/python3

def best_score(a_dictionary):
    values = []
    keys = []
    if isinstance(a_dictionary, dict):
        for key, value in a_dictionary.items():
            keys.append(key)
            values.append(value)
        if len(values) == 0:
            return
        else:
            return keys[values.index(max(values))]
