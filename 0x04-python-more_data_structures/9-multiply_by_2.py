#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for val in a_dictionary:
        new_v = a_dictionary[val] * 2
        a_dictionary[val] = new_v
    return a_dictionary
