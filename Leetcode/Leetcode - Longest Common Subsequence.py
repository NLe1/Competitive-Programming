"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    count[i + 1][j + 1] = 1 + count[i][j]
                else:
                    count[i + 1][j + 1] = max(count[i][j + 1], count[i + 1][j])
        return count[-1][-1]

s = Solution()
print(s.longestCommonSubsequence("abcde", "abc"))
