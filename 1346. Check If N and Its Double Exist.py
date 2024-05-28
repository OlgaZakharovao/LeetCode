'''
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
'''

def checkIfExist(arr: list[int]) -> bool:
    ans = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]*2 and i != j:
                ans = True
    return ans


arr = [3,1,7,11]
print(checkIfExist(arr))
