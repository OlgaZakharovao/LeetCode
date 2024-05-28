'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
'''

# Решить с помощью рекурсии


def isPowerOfFour(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    else:
        return isPowerOfFour(n // 4)


n = 1024
print(isPowerOfFour(n))