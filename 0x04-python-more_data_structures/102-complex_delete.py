#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new_dict = {k: v for k, v in a_dictionary.items() if v != value}
    return (new_dict)
