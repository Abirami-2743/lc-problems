"""
2798. Number of Employees Who Met the Target

There are n employees in a company, numbered from 0 to n - 1. You are
given an array hours of length n and a non-negative integer target.
hours[i] denotes the number of hours worked by employee i. Return the
integer denoting the number of employees who worked at least target
hours.

Example 1:
Input: hours = [0,1,2,3,4], target = 2
Output: 3

Example 2:
Input: hours = [5,1,4,2,2], target = 6
Output: 0
"""


def number_of_employees_who_met_target(hours, target: int) -> int:
    return sum(1 for h in hours if h >= target)



