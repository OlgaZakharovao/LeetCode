'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can
be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''


def longestPalindrome(s) -> int:
    d = {}
    ans = 0
    for i in range(len(s)):
        # if s[i] not in d.keys():
        #     d[s[i]] = 1
        # else:
        #     d[s[i]] += 1
        d[s[i]] = d.get(s[i], 0) + 1
    for value in d.values():
        if value % 2 == 0:
            ans += value
        else:
            ans += value - 1

    if ans < len(s):
        ans += 1
    return ans


s = "a"
print(longestPalindrome(s))

