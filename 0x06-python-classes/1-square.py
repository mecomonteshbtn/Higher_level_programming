#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:23:37 2020

@author: meco
"""


class Square:
    """Define a class for Square

    Instatation with size of the square

    Attributes:
        size: a private instance
    """
    def __init__(self, size):
        self.__size = size
