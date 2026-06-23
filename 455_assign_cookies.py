"""
455. Assign Cookies

You are given two integer arrays g and s, where g[i] is the greed factor
of the ith child, and s[j] is the size of the jth cookie. Each child can
get at most one cookie, and a cookie of size s[j] can satisfy a child
with greed factor g[i] if and only if s[j] >= g[i]. Return the maximum
number of content children.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
"""


def find_content_children(g, s) -> int:
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i


if __name__ == "__main__":
    print(find_content_children([1, 2, 3], [1, 1]))
    print(find_content_children([1, 2], [1, 2, 3]))
