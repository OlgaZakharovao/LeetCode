'''
Given a string s, return the longest
palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''


def longestPalindrome(self, s):
    p = ''
    for i in range(len(s)):
        p1 = self.get_palindrome(s, i, i + 1)
        p2 = self.get_palindrome(s, i, i)
        p = max([p, p1, p2], key=len)
    return p


def get_palindrome(self, s: str, l: int, r: int) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]

s = input()
print(longestPalindrome(s))
