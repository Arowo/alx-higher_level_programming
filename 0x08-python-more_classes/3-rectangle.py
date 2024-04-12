#!/usr/bin/python3
""""
Module 2-rectangle
Define class Rectangle
"""


class Rectangle:
    """
    class Rectangle definition

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """

    def __init__(self, width=0, height=0):
        """"
        Initiliaze rectangles

        Attributes:
            __width (int): private attribute
            __height (int): private attribute
        Raises:
            TyperError: if width and height is not int type
            ValueError: if width and height is < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter

        Return:width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value (int): set width to value if > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value: set height to value if >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return: area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return: perimeter of rectangle if width or height is != 0"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)
