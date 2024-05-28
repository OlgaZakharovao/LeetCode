'''
Given an integer x, return true if x is a
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
'''

# Со строками
def isPalindrome(x):
    return str(x) == str(x)[::-1]


# Без строк
def isPalindrome1(x):
    default_num = x
    if x < 0:
        return False
    new_x = 0
    while x != 0:
        new_x = new_x * 10 + x % 10
        x = x // 10
    return default_num == new_x

x = 121
print(isPalindrome(x))

print(isPalindrome1(x))
