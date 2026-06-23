"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
Return the number of unique elements.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""


def remove_duplicates(nums) -> int:
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == "__main__":
    a = [1, 1, 2]
    print(remove_duplicates(a), a[:2])  
    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(b), b[:5])  