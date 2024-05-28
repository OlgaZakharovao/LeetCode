'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''
'''
def maxVowels(s, k):
    start = 0
    vowels = "aeiou"
    substring = ""
    ans = 0
    while start < len(s) - k+1:
        cur_counter = 0
        for i in range(start, len(s)):
            if len(substring) < k:
                substring += s[i]
            else:
                break
        start += 1
        for i in range(len(substring)):
            if substring[i] in vowels:
                cur_counter += 1
        if cur_counter > ans:
            ans = cur_counter
        substring = ""
    return ans
'''


def maxVowels(s, k):
    s_list = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    cur_counter = 0
    for i in range(k):
        if s_list[i] in vowels:
            cur_counter += 1
    max_num = cur_counter
    for i in range(k, len(s)):
        start = i - k + 1
        if s_list[start-1] in vowels:
            cur_counter = cur_counter - 1
        if s_list[i] in vowels:
            cur_counter = cur_counter + 1
        max_num = max(max_num, cur_counter)
    return max_num



s = input()
k = int(input())
print(maxVowels(s, k))
