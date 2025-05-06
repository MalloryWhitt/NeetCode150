"""
Problem: Longest Consecutive Sequence
Difficulty: Medium

Approach:
- Use a hash set to store all unique numbers from the input list for O(1) lookups.
- Initialize a variable `longest` to track the length of the longest consecutive sequence.
- Iterate through each number in the input list:
  - If the current number is the start of a sequence (i.e., `n - 1` is not in the set), start a new sequence.
  - Use a `length` variable to count the length of the sequence by checking consecutive numbers (`n + length`) in the set.
  - Update `longest` with the maximum of its current value and the length of the current sequence.
- Return `longest` as the length of the longest consecutive sequence.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest