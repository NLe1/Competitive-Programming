"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

import collections
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        d = collections.defaultdict(list)
        for str in strs:
            key = ''.join(sorted(list(str)))
            d[key].append(str)
        return list(d.values())

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))