#!/usr/bin/python3
"""
MyInt Module
"""


class MyInt(int):
    """ MyInt class inverts == with != """
    def __eq__(self, value):
        """ equal to """
        return not super().__eq__(value)

    def __ne__(self, value):
        """ not equal to """
        return not super().__ne__(value)
