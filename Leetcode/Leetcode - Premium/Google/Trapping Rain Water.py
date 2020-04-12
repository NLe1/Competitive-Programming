"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) <= 2: return 0
        count, n = 0 ,len(height)
        leftMax, rightMax = [height[0]] * len(height), [height[-1]] * n
        for i in range(1, len(height)): leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(n-2, -1, -1): rightMax[i] = max(rightMax[i+1], height[i])
        for i, h in enumerate(height):
            shorter = min(leftMax[i], rightMax[i])
            count += (shorter - h)
        return count

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))