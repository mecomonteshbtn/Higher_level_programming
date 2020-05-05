#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers to STDOUT
    """
    for row in matrix:
        row_len = len(row)
        for i in range(row_len):
            if i != row_len - 1:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]), end='')
        print()
