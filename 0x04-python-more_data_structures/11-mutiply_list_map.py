#!/usr/bin/python3


def mutiply_list_map(my_list=[], number=0):
    """
    return a list with all values multiplied by a number using map
    """
    return (list(map(lambda x: x*number, my_list)))
