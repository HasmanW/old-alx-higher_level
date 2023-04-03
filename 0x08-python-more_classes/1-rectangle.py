#!/usr/bin/python3
"""
rectangle class module
"""


class Rectangle:
    """
    class rectangle object
    """
    def __init__(self, width=0, height=0):
        """
        Initializes objects of the class
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ gets the width of the rectangle """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ gets the height of the rectangle """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
