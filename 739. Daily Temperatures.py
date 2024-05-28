'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is
the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which
this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    '''
    ans = []
    for i in range(len(temperatures)):
        for j in range(i+1,len(temperatures)):
            if temperatures[j] > temperatures[i]:
                break
        if temperatures[j] > temperatures[i]:
            ans.append(j-i)
        else:
            ans.append(0)
    return ans
'''
    stack = []
    ans = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            ans[index] = i - index
        stack.append(i)
    return ans


temperatures = [30,60,90]
print(dailyTemperatures(temperatures))
