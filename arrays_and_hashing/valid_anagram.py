"""
Problem: Valid Anagram
Difficulty: Easy

Approach:
- First, check if the lengths of the two strings are different. If they are, return False immediately.
- Use a fixed-size array of length 26 (for each letter in the alphabet) to count the frequency of characters in both strings.
- Iterate through both strings simultaneously:
  - Increment the count for the character in the first string.
  - Decrement the count for the character in the second string.
- After processing both strings, check if all values in the count array are zero.
  - If they are, the strings are anagrams; return True.
  - Otherwise, return False.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True