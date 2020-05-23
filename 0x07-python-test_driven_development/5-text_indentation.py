#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:43:34 2020

@author: Robinson Montes
"""


def text_indentation(text):
    """
    prints a string with 2 new lines after '.', '?', and ':'

    Args:
        text (int): text to print

    Raises:
        TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    string = ""
    while i < len(text) - 1:
        if text[i] in ['.', '?', ':'] and text[i + 1] in " \t\b\a":
            string += text[i] + '\n\n'
            i += 1
        elif text[i] in ['.', '?', ':'] and text[i + 1] not in " \t\b\a":
            string += text[i] + '\n\n'
        else:
            string += text[i]
        i += 1
    string += text[i]

    print("{}".format(string), end='')
