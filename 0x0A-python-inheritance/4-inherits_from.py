#!/usr/bin/python3
"""
module inherits from
"""


def inherits_from(obj, a_class):
    """ checks for subclass"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
