"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.defaultdict(list)
        for i, ch in enumerate(s):
            c[ch].append(i)
        group = [c[key][0] for key in c if len(c[key]) == 1]
        return min(group) if len(group) > 0 else -1

s = Solution()
print(s.firstUniqChar("leetcode"))