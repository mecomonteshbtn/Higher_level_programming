#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020

@author: meco
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Constructor for Square

        Attribute:
            size (int): The size of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        str method for class Square

        Return:
            The string: [class_name] (id) x/y - size
        """
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.size)
        return string

    def update(self, *args, **kwargs):
        """
        Updates Square class

        Attribute:
            args (list): inputted arguments to updating rectangle class
            kwargs (dict): inputted arguments tu updating rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation for Square attributes

        Return:
            A dictionary representation
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def to_csv(self):
        """
        Creates a list with Square attributes

        Return:
            A Square attributes' list for csv file
        """
        return [self.id, self.size, self.x, self.y]

    @property
    def size(self):
        """
        Property method for size value

        Return:
            Private value size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size value

        Attribute:
            value (int): value to check if is int and gratter than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
