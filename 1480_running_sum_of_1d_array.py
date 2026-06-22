"""
1480. Running Sum of 1d Array

Given an array nums, return the running sum of nums, where
runningSum[i] = sum(nums[0]...nums[i]).

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""


def running_sum(nums):
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


if __name__ == "__main__":
    print(running_sum([1, 2, 3, 4]))        # [1,3,6,10]
    print(running_sum([1, 1, 1, 1, 1]))     # [1,2,3,4,5]
    print(running_sum([3, 1, 2, 10, 1]))    # [3,4,6,16,17]
