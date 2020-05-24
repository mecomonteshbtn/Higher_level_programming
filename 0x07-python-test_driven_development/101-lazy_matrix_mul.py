#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:43:34 2020

@author: Robinson Montes
"""
from numpy import matmul


def check_matrix(matrix, name):
    """
    Check if list of list is a matrix of integer/float

    Args:
        matrix (list of list): list of list of int or float
        name (str): matrix name to test

    Raises:
        TypeError: Exception if elements in matrix and div are not integer or
            float; Each row in the matrix have the same size

    Return:
        matrix if input is a matrix

    """
    if type(matrix) is list:
        if len(matrix) == 0:
            raise ValueError(name + " can't be empty")
        for row in matrix:
            if type(row) is list:
                if len(row) == 0:
                    raise ValueError(name + " can't be empty")
                else:
                    for ele in row:
                        if type(ele) not in [int, float]:
                            raise TypeError(name + " should contain only" +
                                            " integers or floats")
            elif type(row) is not list:
                raise TypeError(name + " must be a list of lists")
            elif len(row) == 0:
                raise ValueError(name + " can't be empty")
            if len(row) != len(matrix[0]):
                raise TypeError("each row of " + name + " must be of the" +
                                " same size")
    else:
        raise TypeError(name + " must be a list")


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix

    Args:
        m_a (list): First matrix
        m_b (list): second matrix

    Returns:
        The result of multiply m_a by m_b

    """
    check_matrix(m_a, 'm_a')
    check_matrix(m_b, 'm_b')
    cols_a = len(m_a[0])
    rows_b = len(m_b)

    if cols_a == rows_b:
        return matmul(m_a, m_b)
    else:
        raise ValueError("m_a and m_b can't be multiplied")
