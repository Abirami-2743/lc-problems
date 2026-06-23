"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even
number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2

Example 2:
Input: nums = [555,901,482,1771]
Output: 1
"""


def find_numbers(nums) -> int:
    return sum(1 for n in nums if len(str(n)) % 2 == 0)


