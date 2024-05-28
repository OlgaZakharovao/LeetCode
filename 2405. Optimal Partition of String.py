'''
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.



Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
'''


def partitionString(s: str) -> int:
    cur_substr = ""
    ans = 0
    for i in range(len(s)):
        if s[i] not in cur_substr:
            cur_substr += s[i]
        else:
            cur_substr = s[i]
            ans += 1
    if len(cur_substr) != 0:
        ans += 1
    return ans


s = "abacaba"
print(partitionString(s))
