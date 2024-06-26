'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
'''


def isHappy(n):
    new_num = 0
    used_num = set()
    while n != 1:
        while n > 0:
            new_num += (n % 10) ** 2
            n //= 10

        if new_num in used_num:
            return False
        used_num.add(new_num)
        n = new_num
        new_num = 0
    if n == 1:
        return True


n = int(input())
print(isHappy(n))
