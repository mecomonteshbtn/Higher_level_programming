#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    replaces all occurances of search with replace
    """
    return ([elem if elem != search else replace for elem in my_list])
