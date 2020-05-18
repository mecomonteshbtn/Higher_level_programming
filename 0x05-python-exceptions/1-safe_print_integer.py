#!/usr/bin/python3


def safe_print_integer(value):
    """
    prints a list of anything, but only prints the integers
    Returns the amount of integers printed
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
