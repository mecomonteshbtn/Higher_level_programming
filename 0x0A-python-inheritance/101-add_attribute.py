#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:13:37 2020

@author: Robinson Montes
"""


def add_attribute(obj, name, value):
    """
    Add attribute into the class if it's possible

    Arguments:
        obj (object): The object to set as attribute
        name (str): Name for the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")

    object.__setattr__(obj, name, value)
