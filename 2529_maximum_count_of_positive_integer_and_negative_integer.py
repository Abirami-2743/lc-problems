"""
2529. Maximum Count of Positive Integer and Negative Integer

Given an array nums sorted in non-decreasing order, return the maximum
between the number of positive integers and the number of negative
integers. In other words, if the number of positive integers in nums is
pos and the number of negative integers is neg, then return the maximum
of pos and neg. Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
"""


def maximum_count(nums) -> int:
    pos = sum(1 for n in nums if n > 0)
    neg = sum(1 for n in nums if n < 0)
    return max(pos, neg)


