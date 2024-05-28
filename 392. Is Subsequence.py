'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''


def isSubsequence(s, t) -> bool:
    if s == "":
        return True
    list_s = list(s)
    index_s = 0
    list_t = list(t)
    word = ""
    flg = 1
    while flg == 1:
        flg = 0
        for i in range(len(list_t)):
            if list_t[i] == list_s[index_s]:
                word += list_t[i]
                flg = 1
                list_t[i] = 0
                index_s += 1
            if s == word:
                return True
        word = ""
        index_s = 0
    return False



s = ""
t = "ahbgdc"
print(isSubsequence(s,t))
