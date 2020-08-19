#!/usr/bin/python3
"""Script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy.
"""


def find_peak(list_of_integers):
    """
    Return the peak in a list of integers
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
