'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

import numpy as np


def spiralOrder(matrix):
    ans = []
    while len(matrix) > 0:
        ans += matrix[0]
        matrix = np.transpose(matrix[1:])[::-1].tolist()
    return ans


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
print(spiralOrder(matrix))
