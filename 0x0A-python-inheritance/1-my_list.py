#!/usr/bin/python3
"""
my list module
"""


class MyList(list):
    """ class inherits from list class """
    def print_sorted(self):
        """ prints a sorted list"""
        print(sorted(self))
