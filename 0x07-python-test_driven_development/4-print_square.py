#!/usr/bin/python3
""" print square module """


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        TypeError("size must be an integer")

    for x in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
