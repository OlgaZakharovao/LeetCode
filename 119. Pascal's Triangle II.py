'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
'''


def getRow(rowIndex: int) -> list[int]:
    l = [1, 1]
    if rowIndex == 0:
        return [1]
    while len(l) < rowIndex+1:
        cur = [1]
        for i in range(len(l) - 1):
            cur.append(l[i] + l[i + 1])
        cur.append(1)
        l = cur
    return l


rowIndex = 0
print(getRow(rowIndex))

