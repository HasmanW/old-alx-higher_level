#!/usr/bin/python3
"""
rectangle class module
"""


class Rectangle:
    """
    class rectangle object
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes objects of the class
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __str__(self):
        """ prints rectangle with character # """
        if self.__width == 0 or self.__height == 0:
            return ""
        new_str = ""
        for height in range(self.__height):
            for width in range(self.__width):
                try:
                    new_str += str(self.print_symbol)
                except Exception:
                    new_str += type(self).print_symbol
            new_str += "\n"
        return new_str

    def __repr__(self):
        """ repr representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ detects a deletion """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the bigger rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a rectangle """
        return Rectangle(size, size)
