"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

import itertools
import collections
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 0: return 0
        groups = [[num, len(list(group))] for num, group in itertools.groupby(s)]
        ans , d = float("-inf"), collections.defaultdict(int)
        left, right = 0, 0
        for chr, freq in groups:
            d[chr] += freq
            while len(d) >= 3:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            ans = max(ans, sum(d.values()))
        return ans

s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eceba"))