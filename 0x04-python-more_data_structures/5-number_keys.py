#!/usr/bin/python3

def number_keys(a_dictionary):
    keys = []
    for key, value in a_dictionary.items():
        keys.append(key)
    return len(keys)
