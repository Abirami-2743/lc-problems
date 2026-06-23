"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements. Do this
in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


def move_zeroes(nums) -> None:
    insert_pos = 0
    for n in nums:
        if n != 0:
            nums[insert_pos] = n
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0


