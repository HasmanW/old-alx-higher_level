#!/usr/bin/python3
"""
module kind of
"""


def is_kind_of_class(obj, a_class):
    """ checks if same class or subclass """
    if isinstance(obj, a_class):
        return True
    else:
        return False
