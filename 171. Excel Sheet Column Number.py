'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

A - 65 Z - 90
'''


def titleToNumber(columnTitle: str) -> int:
    l = len(columnTitle)
    s = len(columnTitle)
    ans = 0
    for i in range(l):
        ans += (ord(columnTitle[i]) - 64) * 26 ** (s - 1)
        s -= 1
    return ans


columnTitle = "ZY"
print(titleToNumber(columnTitle))
