'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''


def myPow(x: float, n: int) -> float:
    if n < 0:
        n = -n
        x = 1/x
    if n == 0:
        return 1
    if n == 1:
        return x
    elif n > 0:
        if n % 2 == 0:
            return myPow(x**2, n//2)
        else:
            return x * myPow(x ** 2, (n - 1) // 2)
    # elif n < 0:
    #     if n % 2 == 0:
    #         return myPow(x**2, n // 2)
    #     else:
    #         return 1/x * myPow(x ** 2, (n + 1) // 2)


x = 2.00000
n = -2
print(myPow(x, n))









