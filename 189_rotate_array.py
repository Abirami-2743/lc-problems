"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""


def rotate(nums, k: int) -> None:
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k] if k else nums[:]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    print(a)  # [5,6,7,1,2,3,4]

    b = [-1, -100, 3, 99]
    rotate(b, 2)
    print(b)  # [3,99,-1,-100]
