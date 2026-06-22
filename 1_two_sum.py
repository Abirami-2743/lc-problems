"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target. You may assume that
each input would have exactly one solution, and you may not use the same
element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


def two_sum(nums, target: int):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))       # [1, 2]
    print(two_sum([3, 3], 6))          # [0, 1]
