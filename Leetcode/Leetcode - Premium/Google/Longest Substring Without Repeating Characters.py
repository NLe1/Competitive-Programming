"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, i, cache,  = 0, 0, dict()
        for j, chr in enumerate(s):
            if chr in cache and cache[chr] >= i:
                i = cache[chr] + 1
            cache[chr] = j
            ans = max(ans, j - i + 1)
        return ans
s = Solution()
print(s.lengthOfLongestSubstring("abba"))


