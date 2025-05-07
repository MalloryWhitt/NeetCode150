"""
Problem: Container With Most Water
Difficulty: Medium

Approach:
- Use the two-pointer technique to find the maximum area between two lines.
- Initialize two pointers:
  - `l` pointing to the beginning of the array.
  - `r` pointing to the end of the array.
- Initialize a variable `res` to store the maximum area found.
- While `l` is less than `r`:
  - Calculate the area formed by the lines at `l` and `r` using the formula:
    `area = (r - l) * min(height[l], height[r])`.
  - Update `res` with the maximum of its current value and the calculated `area`.
  - Move the pointer pointing to the shorter line inward:
    - If `height[l] < height[r]`, increment `l`.
    - Otherwise, decrement `r`.
- Return `res` as the maximum area.
"""

class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res