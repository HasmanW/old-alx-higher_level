#!/usr/bin/python3

def safe_print_integer(value):
    """ prints integers """
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
            return True
        except TypeError:
            return False
