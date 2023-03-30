#!/usr/bin/python3

def safe_print_integer(value):
    """ prints integers """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
