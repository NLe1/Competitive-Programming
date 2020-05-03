"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""


class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        if len(nums) <= 1: return 0
        d = {0 : [-1, -1]}
        count = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in d: d[count] = [d[count][0], i]
            else: d[count] = [i,i]
        m = float('-inf')
        for start,end in d.values():
            m = max(m, end-start)
        return m

s = Solution()
print(s.findMaxLength([0,0,0,1,0,0,0,0]))