"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false
otherwise.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false

Example 3:
Input: x = 10
Output: false
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))   # True
    print(is_palindrome(-121))  # False
    print(is_palindrome(10))    # False
