'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is
exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible
subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing
the order of the remaining elements.


Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
'''


'''
def findLHS(nums):
    nums_nums = nums.copy()
    nums_hold = []
    final_ans = []
    cur_ans = []
    index1 = 0
    index2 = 0
    while max(index1, index2) < len(nums):
        num1 = nums[max(index1, index2)]
        num2 = nums[max(index1, index2) + 1]
        index = 0
        if abs(num1 - num2) <= 1:
            maximum = max(num1, num2)
            minimum = min(num1, num2)
        else:
            num1 = 'a'
            num2 = 'b'
            flg = 0
            for i in range(1, len(nums)):
                if num1 != 'a' and flg == 1:
                    num2 = nums[i]
                    flg = 2
                if flg == 0:
                    num1 = nums[i]
                    flg = 1
                if flg == 2 and abs(num1-num2) <= 1:
                    maximum = max(num1, num2)
                    minimum = min(num1, num2)
                    index = i + 1
                    break
        index1 = nums.index(maximum)
        index2 = nums.index(minimum)
        index3 = index
        if index1 > index2:
            cur_ans.append(minimum)
            cur_ans.append(maximum)
        else:
            cur_ans.append(maximum)
            cur_ans.append(minimum)
        nums[min(index1, index2)] = 'l'
        nums[max(index1, index2)] = 'k'
        for i in range(index, len(nums)):
            if nums[i] + 1 == maximum or nums[i] - 1 == minimum:
                cur_ans.append(nums[i])
                index3 += 1
            else:
                if len(cur_ans) > len(final_ans):
                    final_ans = cur_ans
                    cur_ans = []
                break

        nums_hold = nums.copy()
        nums = nums_nums
        nums_nums = nums_hold.copy()
    if len(cur_ans) > len(final_ans):
        final_ans = cur_ans
    return len(final_ans)
'''


from collections import Counter


def findLHS(nums):
    repetitions = dict(Counter(nums))
    ans = 0
    sorted_keys = sorted(repetitions.keys())
    for i in sorted_keys:
        if i + 1 in sorted_keys and repetitions[i] + repetitions[i+1] > ans:
            ans = repetitions[i] + repetitions[i+1]
    return ans


nums = [1,1,1,1]
print(findLHS(nums))
