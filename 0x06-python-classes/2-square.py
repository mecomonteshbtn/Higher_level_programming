#!/usr/bin/python3


class Square:
    """
    class square with attributes:
        size as Private
    """
    def __init__(self, size=0):
        """
        the initialization with opotional size and checks for
        input errors for size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
