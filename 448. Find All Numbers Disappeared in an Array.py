'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
'''

def findDisappearedNumbers(nums):
    nums = sorted(nums)
    ans = []
    prev_num = nums[0]
    for i in range(1, nums[0]):
        ans.append(i)
    for i in range(len(nums)):
        if nums[i] > prev_num + 1:
            while prev_num + 1 != nums[i]:
                ans.append(prev_num+1)
                prev_num += 1
        prev_num = nums[i]
    if nums[-1] != len(nums):
        maximum = nums[-1]
        for i in range(maximum, len(nums)):
            ans.append(i + 1)
    return ans


nums = [5,4,6,7,9,3,10,9,5,6]
print(findDisappearedNumbers(nums))
