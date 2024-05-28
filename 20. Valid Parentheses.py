'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''


def isValid(s: str) -> bool:
    list_s = list(s)
    left = []
    for i in range(len(list_s)):
        if list_s[i] in "({[":
            left.append(list_s[i])
        else:
            if len(left) > 0:
                last = left.pop()
                if (last == '(' and list_s[i] == ')') or (last == '{' and list_s[i] == '}') \
                        or (last == '[' and list_s[i] == ']'):
                    continue
                else:
                    return False
            else:
                return False
    if len(left) == 0:
        return True
    else:
        return False


s = "[["
print(isValid(s))

