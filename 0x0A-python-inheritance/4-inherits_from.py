#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:13:37 2020

@author: Robinson Montes
"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of class, or if the object is an instance\
        of a class that inherited from
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
