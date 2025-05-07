"""
Problem: 3 Sum
Difficulty: Medium

Approach:
- Sort the input array to simplify finding triplets and handling duplicates.
- Iterate through the array with an index `i`:
  - Skip duplicate values for the current number to avoid duplicate triplets.
  - Use two pointers (`l` and `r`) to find pairs that sum up to the negative of the current number (`-nums[i]`):
    - Initialize `l` to `i + 1` and `r` to the end of the array.
    - Calculate the sum of the triplet (`threeSum = nums[i] + nums[l] + nums[r]`).
    - If `threeSum` is greater than 0, decrement the right pointer (`r -= 1`).
    - If `threeSum` is less than 0, increment the left pointer (`l += 1`).
    - If `threeSum` equals 0, add the triplet to the result list and move the left pointer while skipping duplicates.
- Return the result list containing all unique triplets that sum up to 0.
"""

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
        