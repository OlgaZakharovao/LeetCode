'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]
        cur_parenthesis = self.generateParenthesis(n-1)
        new_parenthesis = []
        for i in range(len(cur_parenthesis)):
            if "()" + cur_parenthesis[i] not in new_parenthesis:
                new_parenthesis.append("()" + cur_parenthesis[i])
            if cur_parenthesis[i] + "()" not in new_parenthesis:
                new_parenthesis.append(cur_parenthesis[i] + "()")
            new_parenthesis.append("(" + cur_parenthesis[i] + ")")
        return new_parenthesis


s = Solution()
n = 3
# print(s.generateParenthesis(n))




a = ["()()()()","(()()())","()(()())","(()())()","((()()))","()()(())","()(())()","(()(()))","(())()()","((())())","()((()))","((()))()","(((())))"]

b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

for i in b:
    if i not in a:
        print(i)
