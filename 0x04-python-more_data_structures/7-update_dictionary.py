#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    keys = []
    for k, v in a_dictionary.items():
        keys.append(k)
    if key in keys:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
