#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for val in keys:
        if value == a_dictionary.get(val):
            del a_dictionary[val]
    return a_dictionary
