'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


def longestCommonPrefix(strs:list[str]):
    if len(strs) == 0:
        return ""
    min_word = min(strs, key=len)
    min_prefix = len(min_word)
    for i in range(len(strs)):
        max_prefix = 0
        for j in range(len(min_word), -1, -1):
            if strs[i].startswith(min_word[:j]) and j > max_prefix:
                max_prefix = j
        if max_prefix < min_prefix:
            min_prefix = max_prefix
    return min_word[:min_prefix]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
