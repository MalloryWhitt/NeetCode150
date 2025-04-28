"""
Problem: Encode and Decode Strings
Difficulty: Medium

Approach:
**Encode:**
- Iterate through the list of strings.
- For each string, append its length followed by a delimiter (`#`) and the string itself to the result.
- Return the concatenated result as the encoded string.

**Decode:**
- Use a pointer `i` to traverse the encoded string.
- For each substring:
  - Find the delimiter (`#`) to determine the length of the next string.
  - Extract the substring of the given length and append it to the result list.
  - Move the pointer to the next position after the extracted substring.
- Return the list of decoded strings.
"""

from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res