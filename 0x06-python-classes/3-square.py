#!/usr/bin/python3
"""size validation"""


class Square:
    """class defines a square"""
    __size = 0

    def __init__(self, size=0):
        """set size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """find area of a square"""
        return self.__size * self.__size
