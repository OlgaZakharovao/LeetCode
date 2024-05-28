'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for
space complexity analysis.)
'''


def productExceptSelf(nums: list[int]) -> list[int]:
    '''
    Тоже работает
    mult = 1
    ans = []
    flg = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            mult *= nums[i]
        else:
            flg += 1
    for index in range(len(nums)):
        if nums[index] == 0 and flg < 2:
            ans.append(mult)
        elif flg > 1:
            ans.append(0)
        else:
            if flg == 1:
                ans.append(0)
            else:
                ans.append(mult // nums[index])
    return ans
    '''
    ans = [0] * len(nums)
    mult = 1
    for i in range(len(nums)):
        ans[i] = mult
        mult *= nums[i]
    mult = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= mult
        mult *= nums[i]
    return ans


nums = [1,2,3,4]
print(productExceptSelf(nums)) #[[24,12,8,6]]
