#!/usr/bin/python3


def no_c(my_string):
    """
    removes all characters 'c' and 'C' from s
    """
    new_str = ""
    for i in my_string:
        if i not in "cC":
            new_str += i
    return (new_str)
