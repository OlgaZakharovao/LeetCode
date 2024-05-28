'''
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.



Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
'''



def integerReplacement(n):
    ans = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            ans += 1
        else:
            divide_plus = 0
            divide_minus = 0
            new_n_plus1 = n+1
            new_n_minus1 = n-1
            while new_n_plus1 % 2 == 0:
                divide_plus += 1
                new_n_plus1 = new_n_plus1 / 2
            while new_n_minus1 % 2 == 0:
                divide_minus += 1
                if new_n_minus1 / 2 == 1 and divide_minus < divide_plus:
                    return ans + divide_minus + 1
                else:
                    new_n_minus1 = new_n_minus1 / 2
            if divide_plus >= divide_minus:
                n = (n+1)/2
                ans += 2
            else:
                n = (n-1)/2
                ans += 2
    return ans


n = int(input())
print(integerReplacement(n))
