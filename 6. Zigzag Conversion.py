'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''


def convert(s, numRows):
    if numRows == 1:
        return s
    strings = [[] for i in range(numRows)]
    rev = False
    count = -1

    for i in range(len(s)):
        if not rev:
            count += 1
        else:
            count -= 1
        strings[count].append(s[i])
        if count == numRows - 1:
            rev = True
        elif count == 0:
            rev = False

    zigzag = ""
    for string in strings:
        zigzag += ''.join(string)
    return zigzag


s = input()
numRows = int(input())
print(convert(s, numRows))
