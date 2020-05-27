#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 2020
@author: Robinson Montes
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
