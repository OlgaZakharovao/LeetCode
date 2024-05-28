'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''


def reverse(x: int) -> int:
    x_new = str(x)
    x_without_zero = ""
    ans = ""
    flg = 0
    if x_new[0] == '-':
        ans += '-'
        x_new = x_new[1:]
    for i in range(len(x_new) - 1, -1, -1):
        if x_new[i] == 0 and flg == 0:
            continue
        else:
            x_without_zero += x_new[i]
            flg = 1

    if int(ans + x_without_zero) > 2**31 - 1 or int(ans + x_without_zero) < -2**31:
        return 0
    return int(ans + x_without_zero)


x = 1534236469
print(reverse(x))
