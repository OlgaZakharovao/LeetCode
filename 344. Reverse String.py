'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


def reverseString(s) -> None:
    left = 0
    while (left != len(s) - left - 1 or (len(s) - left - 1 - left < 1 and len(s) % 2 == 0)) and left < len(s)/2:
        s[left], s[len(s) - left - 1] = s[len(s) - left - 1], s[left]
        left += 1

s = ["H","a","n","n","a","h"]
print(reverseString(s))

