"""
Problem: Trapping Rain Water
Difficulty: Hard

Approach:
- Use the two-pointer technique to calculate the amount of trapped rainwater.
- Initialize two pointers:
  - `l` pointing to the beginning of the array.
  - `r` pointing to the end of the array.
- Initialize variables `leftMax` and `rightMax` to track the maximum height seen so far from the left and right, respectively.
- Initialize a variable `res` to store the total amount of trapped water.
- While `l` is less than `r`:
  - If `leftMax` is less than or equal to `rightMax`:
    - Move the left pointer inward (`l += 1`).
    - Update `leftMax` to the maximum of its current value and `height[l]`.
    - Add the difference between `leftMax` and `height[l]` to `res` (if positive).
  - Otherwise:
    - Move the right pointer inward (`r -= 1`).
    - Update `rightMax` to the maximum of its current value and `height[r]`.
    - Add the difference between `rightMax` and `height[r]` to `res` (if positive).
- Return `res` as the total amount of trapped rainwater.
"""

class Solution(object):
    def trap(self, height):
        
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res