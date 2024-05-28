'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
'''


def increasingTriplet(nums: list[int]) -> bool:
    last_last = float('inf')
    last = float('inf')
    for num in nums:
        if num > last_last:
            last = min(num, last)
        else:
            last_last = min(num, last_last)
        if num > last:
            return True
    return False


nums = [2,1,5,0,4,6]
print(increasingTriplet(nums))
