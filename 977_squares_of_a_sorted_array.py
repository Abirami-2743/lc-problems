"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1
    return result


if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
    print(sorted_squares([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]
