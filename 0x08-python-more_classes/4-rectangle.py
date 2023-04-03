#!/usr/bin/python3
"""
rectangle class module
"""


class Rectangle:
    """
    class rectangle object
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            new_str = []
            for height in range(self.__height):
                for width in range(self.__width):
                    new_str.append('#')
                new_str.append("\n")
        return "".join(new_str)

    def __repr__(self):
        return f"Rectangle( {str(self.__width)}, {str(self.__height)})"
