'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of
American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".


Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
'''


def findWords(words):
    alphabet1 = "qwertyuiopQWERTYUIOP"
    alphabet2 = "asdfghjklASDFGHJKL"
    alphabet3 = "zxcvbnmZXCVBNM"
    ans = []
    flg = 0
    for word in words:
        if word[0] in alphabet1:
            cur_alphabet = alphabet1
        elif word[0] in alphabet2:
            cur_alphabet = alphabet2
        else:
            cur_alphabet = alphabet3
        for letter in word:
            if letter not in cur_alphabet:
                flg = 1
        if flg == 0:
            ans.append(word)
        flg = 0
    return ans


words = ["adsdf","sfd"]
print(*findWords(words))
