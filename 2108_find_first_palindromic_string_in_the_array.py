"""
2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in
the array. If there is no such string, return an empty string "".

Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"

Example 3:
Input: words = ["def","ghi"]
Output: ""
"""


def first_palindrome(words) -> str:
    for word in words:
        if word == word[::-1]:
            return word
    return ""


