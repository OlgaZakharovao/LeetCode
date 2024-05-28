'''
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word,
and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.


Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters are 'a', 'b', and 'c'.


Example 2:
Input: word = "abc"
Output: 0
Explanation:
There are no special characters in word.


Example 3:
Input: word = "AbBCab"
Output: 0
Explanation:
There are no special characters in word.
'''


def numberOfSpecialChars(word: str) -> int:
    letters_lower = set()
    letters_upper = set()
    deleted_letters = set()
    ans = 0
    for i in range(len(word)):
        if word[i].lower() == word[i] and word[i].upper() in letters_upper:
            ans -= 1
            deleted_letters.add(word[i].lower())
        elif word[i] == word[i].lower():
            letters_lower.add(word[i])
        elif word[i].upper() == word[i] and word[i].lower() not in letters_lower:
            deleted_letters.add(word[i].lower())
            letters_upper.add(word[i])
        elif word[i].upper() == word[i]:
            ans += 1
            letters_upper.add(word[i])
    print(deleted_letters)
    print(letters_upper)
    return len(letters_upper) - len(deleted_letters)


word = "AbBCab"
print(numberOfSpecialChars(word))
