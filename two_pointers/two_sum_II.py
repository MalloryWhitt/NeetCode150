"""
Problem: Two Sum II - Input Array Is Sorted
Difficulty: Medium

Approach:
- Use the two-pointer technique to find the two numbers that add up to the target.
- Initialize two pointers:
  - `l` pointing to the beginning of the array.
  - `r` pointing to the end of the array.
- While `l` is less than `r`:
  - Calculate the sum of the numbers at the two pointers (`curSum = numbers[l] + numbers[r]`).
  - If `curSum` is greater than the target, move the right pointer (`r`) one step to the left.
  - If `curSum` is less than the target, move the left pointer (`l`) one step to the right.
  - If `curSum` equals the target, return the 1-based indices `[l + 1, r + 1]`.
- If no such pair is found, return an empty list.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []