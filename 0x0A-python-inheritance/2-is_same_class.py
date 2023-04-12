#!/usr/bin/python3
"""
same class module
"""


def is_same_class(obj, a_class):
    """ check if obj == class """
    if obj.__class__ is a_class:
        return True
    else:
        return False
