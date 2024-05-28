'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
'''

def tribonacci(n: int) -> int:
    zero = 0
    first = 1
    second = 1
    seq = [0, 1, 1]
    cur_num = 0
    if n == 0:
        return zero
    elif n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(n-2):
            cur_num = seq[-1] + seq[-2] + seq[-3]
            seq[-3] = seq[-2]
            seq[-2] = seq[-1]
            seq[-1] = cur_num
        return(seq[-1])



n = 25
print(tribonacci(n))