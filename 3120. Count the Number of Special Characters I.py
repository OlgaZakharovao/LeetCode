'''
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.



Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.


Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.


Example 3:
Input: word = "abBCab"
Output: 1
Explanation:
The only special character in word is 'b'.
'''


def numberOfSpecialChars(word: str) -> int:
    letters = []
    letters_set = set()
    ans = 0
    for i in range(len(word)):
        if word[i].lower() not in letters and word[i].upper() not in letters:
            letters.append(word[i])
        elif ((word[i].lower() == word[i] and word[i].upper() in letters) \
                or (word[i].upper() == word[i] and word[i].lower() in letters)) and word[i].lower() not in letters_set:
            ans += 1
            letters_set.add(word[i].lower())
    return ans


word = "EDdd"
print(numberOfSpecialChars(word))
