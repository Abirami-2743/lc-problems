"""
704. Binary Search

Given an array of integers nums sorted in ascending order, and an integer
target, write a function to search target in nums. If target exists,
return its index. Otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
"""


def search(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))  
    print(search([-1, 0, 3, 5, 9, 12], 2))  
