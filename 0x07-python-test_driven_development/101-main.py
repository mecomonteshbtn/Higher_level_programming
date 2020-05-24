#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(lazy_matrix_mul([[3, 4], [6, 5]], [[8], [7]]))
print(lazy_matrix_mul([[3.6, -4.5], [-6, 5-3]], [[-0.8], [1.7]]))
