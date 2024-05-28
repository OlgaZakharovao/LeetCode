'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 231 - 1
'''


def addDigits(num):
    ans = 10
    while len(str(ans)) != 1:
        ans = 0
        digits = list(str(num))
        for i in range(len(digits)):
            ans += int(digits[i])
        num = ans
    return ans


num = int(input())
print(addDigits(num))







