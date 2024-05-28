'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''


def generate(numRows: int) -> list[list[int]]:
    l = [[1], [1, 1]]
    if numRows == 1:
        return [[1]]
    while len(l) < numRows:
        prev = l[-1]
        cur = [1]
        for i in range(len(prev) - 1):
            cur.append(prev[i] + prev[i+1])
        cur.append(1)
        l.append(cur)
    return l


numRows = 1
print(generate(numRows))
