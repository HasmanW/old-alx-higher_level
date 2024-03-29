#!/usr/bin/python3
"""
The square module
"""


class Square:
    """
    The square class
    """
    def __init__(self, size=0):
        """
        data initialization
        """
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
