'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

from collections import Counter


def isAnagram(s, t:str):
    if len(s) != len(t):
        return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict == t_dict



s = input()
t = input()
print(isAnagram(s, t))
