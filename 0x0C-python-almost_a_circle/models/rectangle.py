#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020

@author: meco
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constructor for Rectangle

        Attributes:
            width (int): Private attribute for the width of the Rectangle
            height (int): Private attribute for the height of the Rectangle
            x (int): Private attribute for x value of the Rectangle
            y (int): Private attribute for y value of the Rectangle
            id (int): Private attribute id inherits from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints the # char Rectangle
        """
        for i in range(self.height):
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        str method for class Rectangle

        Return:
            The string: [class_name] (id) x/y - width/height
        """
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x, self.y,
                                                  self.width, self.height)
        return string

    @property
    def width(self):
        """
        Property method for width value

        Return:
            Private value width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width value

        Attribute:
            value (int): value to check if is int and gratter than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Property method for height value

        Return:
            Private value height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height value

        Attribute:
            value (int): value to check if is int and gratter than 0
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Property method for x value

        Return:
            Private value x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x value

        Attribute:
            value (int): value to check if is int and gratter than 0
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be > 0')
        self.__x = value

    @property
    def y(self):
        """
        Property method for y value

        Return:
            Private value y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y value

        Attribute:
            value (int): value to check if is int and gratter than 0
        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be > 0')
        self.__y = value
