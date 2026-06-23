"""
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in
this array. If the third maximum does not exist, return the maximum
number.

Example 1:
Input: nums = [3,2,1]
Output: 1

Example 2:
Input: nums = [1,2]
Output: 2

Example 3:
Input: nums = [2,2,3,1]
Output: 1
"""


def third_max(nums) -> int:
    top3 = []
    for n in nums:
        if n in top3:
            continue
        top3.append(n)
        top3.sort(reverse=True)
        if len(top3) > 3:
            top3.pop()
    return top3[-1] if len(top3) == 3 else top3[0]


if __name__ == "__main__":
    print(third_max([3, 2, 1]))     
    print(third_max([1, 2]))        
    print(third_max([2, 2, 3, 1]))  
