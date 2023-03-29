#!/usr/bin/python3
"""
The square module
"""


class Square:
    """ The square class """
    def __init__(self, size=0):
        """ data initialization """
        self.__size = size

    @property
    def size(self):
        """ retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size value """
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
        return self.__size

    def area(self):
        """ returns area of the sqaure """
        square = self.__size * self.__size
        return square
