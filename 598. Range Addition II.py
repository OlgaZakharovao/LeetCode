'''
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means
M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

Example 2:
Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4

Example 3:
Input: m = 3, n = 3, ops = []
Output: 9
'''


def maxCount(m: int, n: int, ops: list[list[int]]) -> int:
    minimum_x = n
    minimum_y = m
    for y, x in ops:
        minimum_x = min(minimum_x, x)
        minimum_y = min(minimum_y, y)
    return minimum_x * minimum_y


m = 3
n = 3
ops = [[2, 2], [3, 3]]
print(maxCount(m, n, ops))
