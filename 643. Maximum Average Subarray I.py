'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any
answer with a calculation error less than 10-5 will be accepted.


Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
'''
#1 2 3 4 5 6 7 8 9


def findMaxAverage(nums: list[int], k) -> float:
    new_nums = nums[:k]
    summa = sum(new_nums)
    prev_sum = summa
    for i in range(1, len(nums) - k + 1):
        new_nums = nums[i:i + k]
        summa = max(prev_sum - nums[i - 1] + nums[i + k-1], summa)
        prev_sum = prev_sum - nums[i - 1] + nums[i + k-1]
    return summa / k


nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))
