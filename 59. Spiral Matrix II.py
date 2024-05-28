'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
'''


def generateMatrix(n):
    res = [[0 for i in range(n)] for j in range(n)]
    left = 0
    right = n - 1
    up = 0
    down = n - 1
    num = 1
    while num <= (n ** 2):
        for x in range(left, right + 1):
            res[up][x] = num
            num += 1
        up += 1

        for i in range(up, down + 1):
            res[i][right] = num
            num += 1
        right -= 1

        if left <= right:
            for i in range(right, left - 1, -1):
                res[down][i] = num
                num += 1
            down -= 1

        if up <= down:
            for i in range(down, up - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
    return res


n = int(input())
print(generateMatrix(n))

