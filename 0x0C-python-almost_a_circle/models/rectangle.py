#!/usr/bin/python3
""" The Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ The rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ returns the width """
        return self.__width

    @property
    def height(self):
        """ returns the height"""
        return self.__height

    @property
    def x(self):
        """ returns value x """
        return self.__x

    @property
    def y(self):
        """ returns value y """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setting and validation """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setting and validation """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setting and validation """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setting and validation """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value



