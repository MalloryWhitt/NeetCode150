"""
Problem: Contains Duplicate
Difficulty: Easy

Approach:
- Use a hash set to store visited numbers.
- Iterate through the list, and for each number, check if it already exists in the hash set.
- If it exists, return True (duplicate found).
- Otherwise, add the number to the hash set.
- If no duplicates are found after iterating through the list, return False.
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
