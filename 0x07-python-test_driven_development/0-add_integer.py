#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b mst be an integer")
    if type(a) is float:
        int(a)
    if type(b) is float:
        int(b)
    return int(a) + int(b)
