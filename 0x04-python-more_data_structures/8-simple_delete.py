#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    keys = []
    for val in a_dictionary:
        keys.append(val)
    if key in keys:
        del a_dictionary[key]
    return a_dictionary
