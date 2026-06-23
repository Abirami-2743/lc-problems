"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's
in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""


def find_max_consecutive_ones(nums) -> int:
    best = current = 0
    for n in nums:
        if n == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


