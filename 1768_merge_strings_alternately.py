"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is
longer than the other, append the additional letters onto the merged
string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
"""


def merge_alternately(word1: str, word2: str) -> str:
    result = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1
    return "".join(result)


if __name__ == "__main__":
    print(merge_alternately("abc", "pqr"))   # apbqcr
    print(merge_alternately("ab", "pqrs"))   # apbqrs
    print(merge_alternately("abcd", "pq"))   # apbqcd
