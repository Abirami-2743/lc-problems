"""
821. Shortest Distance to a Character

Given a string s and a character c that occurs in s, return an array of
integers answer where answer.length == s.length and answer[i] is the
distance from index i to the closest occurrence of character c in s.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]
"""


def shortest_to_char(s: str, c: str):
    n = len(s)
    answer = [0] * n
    prev = float("-inf")
    for i in range(n):
        if s[i] == c:
            prev = i
        answer[i] = i - prev

    prev = float("inf")
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        answer[i] = min(answer[i], prev - i)
    return answer


