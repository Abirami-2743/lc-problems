"""
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:
- All the characters that are not English letters remain in the same
  position.
- All the English letters (lowercase or uppercase) should be reversed.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""


def reverse_only_letters(s: str) -> str:
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)


if __name__ == "__main__":
    print(reverse_only_letters("ab-cd"))                  
    print(reverse_only_letters("a-bC-dEf-ghIj"))          
    print(reverse_only_letters("Test1ng-Leet=code-Q!"))    
