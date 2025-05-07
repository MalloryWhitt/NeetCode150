"""
Problem: Valid Palindrome
Difficulty: Easy

Approach:
- Use two pointers (`l` and `r`) to traverse the string from both ends.
- Skip non-alphanumeric characters by moving the pointers inward until valid characters are found.
- Compare the characters at the two pointers:
  - If they are not equal (ignoring case), return `False` as the string is not a palindrome.
  - Otherwise, move the pointers inward (`l += 1` and `r -= 1`).
- If the entire string is traversed without mismatches, return `True` as the string is a valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True