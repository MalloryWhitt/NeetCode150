"""
Problem: Top K Frequent Elements
Difficulty: Medium

Approach:
- Use a hash map (dictionary) to count the frequency of each number in the input list.
- Create a list of buckets (`freq`), where the index represents the frequency, and each bucket contains the numbers with that frequency.
- Iterate through the hash map and append each number to the corresponding bucket based on its frequency.
- Iterate through the buckets in reverse order (starting from the highest frequency) and collect the top `k` frequent elements.
- Stop collecting elements once `k` elements have been added to the result list.
- Return the result list containing the top `k` frequent elements.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res