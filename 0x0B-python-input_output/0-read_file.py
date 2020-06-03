#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tru Jun 3 15:13:37 2020

@author: Robinson Montes
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
