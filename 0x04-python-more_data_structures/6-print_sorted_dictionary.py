#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = []
    for val in a_dictionary:
        keys.append(val)
    keys.sort()

    for x in keys:
        print("{}: {}".format(x, a_dictionary[x]))
