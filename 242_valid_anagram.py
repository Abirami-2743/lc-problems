"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and
false otherwise. An anagram is a word or phrase formed by rearranging
the letters of a different word or phrase, using all the original
letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


