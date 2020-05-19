#!/usr/bin/python3


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        the initialization function for the square class
        checks for input errors for size
        """
        if self.size(size):
            self.__size = size

    def size(self):
        """
        Property size to retrieve it with a private instance attribute size
        """
        return self.__size

    def size(self, value):
        """
        Property setter size to set it with a private instance attribute size
        Validates if size is greater than 0 and integer type
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Public instance method that returns the current square area
        """
        return self.__size ** 2
