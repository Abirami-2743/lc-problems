"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
Return a string of the words in reverse order, joined by a single space.
The returned string should only have a single space separating the words.
Do not include extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Example 3:
Input: s = "a good   example"
Output: "example good a"
"""


def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])


if __name__ == "__main__":
    print(reverse_words("the sky is blue"))      # blue is sky the
    print(reverse_words("  hello world  "))       # world hello
    print(reverse_words("a good   example"))      # example good a
