"""
Problem: Two Sum
Difficulty: Easy

Approach:
- Use a hash map (dictionary) to store numbers as keys and their indices as values.
- Iterate through the list of numbers:
  - For each number, calculate the difference between the target and the current number (`diff = target - number`).
  - Check if the difference (`diff`) exists in the hash map:
    - If it exists, return the indices of the current number and the number corresponding to `diff` in the hash map.
  - Otherwise, add the current number and its index to the hash map.
- If no such pair is found after iterating through the list, return an empty list.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []