"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of
val in nums in-place. Return the number of elements that are not equal to
val. The order of the remaining elements may be changed.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""


def remove_element(nums, val) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    print(remove_element(nums1, 3), nums1[:2]) 

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    print(remove_element(nums2, 2), nums2[:5])  
