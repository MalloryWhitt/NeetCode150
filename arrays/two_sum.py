"""
Problem: Two Sum
Difficulty: Easy

Approach:
- Use a hash map to store visited numbers and their indices.
- For each number, check if (target - number) exists in map.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# Example
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
