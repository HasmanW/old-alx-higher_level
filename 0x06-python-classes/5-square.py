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
        """ retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size """
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ gets the area of the square """
        square = self.__size * self.__size
        return square

    def my_print(self):
        """ prints the square """
        for _ in range(self.__size):
            for _ in range(self.__size):
                print('#', end="")
            print()
