'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10^(-5) of the actual
answer will be accepted.


Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
'''


def average(salary):
    maximum = 0
    maximum_index = 0
    minimum = salary[0]
    minimum_index = 0

    for i in range(len(salary)):
        if salary[i] > maximum:
            maximum = salary[i]
            maximum_index = i
        elif salary[i] < minimum:
            minimum = salary[i]
            minimum_index = i
    salary.pop(max(maximum_index, minimum_index))
    salary.pop(min(minimum_index, maximum_index))

    summa = 0
    for i in range(len(salary)):
        summa += salary[i]
    return summa / len(salary)


salary = [4000,3000,1000,2000]
#salary = list(map(int, input().split()))
print(average(salary))


