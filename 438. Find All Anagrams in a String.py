'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.



Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import Counter


def findAnagrams(s: str, p: str) -> list[int]:
    n1 = len(s)
    n2 = len(p)
    d1 = Counter(p)
    d2 = Counter(s[:n2 - 1])
    ans = []
    j = 0
    for i in range(n2 - 1, n1):
        d2[s[i]] += 1
        if d1 == d2:
            ans.append(j)
        d2[s[j]] -= 1
        if d2[s[j]] == 0:
            del d2[s[j]]
        j += 1
    return ans


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))


