"""
Problem: Product of Array Except Self
Difficulty: Medium

Approach:
- Initialize a result array (`res`) with all elements set to 1.
- Use a `prefix` variable to calculate the cumulative product of elements to the left of each index:
  - Iterate through the array from left to right.
  - For each index, set `res[i]` to the current value of `prefix` and update `prefix` by multiplying it with `nums[i]`.
- Use a `postfix` variable to calculate the cumulative product of elements to the right of each index:
  - Iterate through the array from right to left.
  - For each index, multiply `res[i]` by the current value of `postfix` and update `postfix` by multiplying it with `nums[i]`.
- Return the `res` array, which contains the product of all elements except the one at each index.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res