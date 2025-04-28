from collections import defaultdict

"""
Problem: Group Anagrams
Difficulty: Medium

Approach:
- Use a hash map (defaultdict) to group anagrams together.
- Iterate through the list of strings:
  - For each string, create a count array of size 26 to represent the frequency of each letter (a-z).
  - Convert the count array to a tuple (to use it as a hashable key) and use it as the key in the hash map.
  - Append the string to the list corresponding to this key in the hash map.
- After processing all strings, return the values of the hash map as a list of lists, where each list contains grouped anagrams.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())