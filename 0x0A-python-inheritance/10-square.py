#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:13:37 2020

@author: Robinson Montes
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class shape, inheirts from Rectangle and BaseGeometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
