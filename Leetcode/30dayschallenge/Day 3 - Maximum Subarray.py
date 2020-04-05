"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        prev, ans  = nums[0], float('-inf')
        for i in range(1, len(nums)):
            ans = max(ans, prev)
            if nums[i] > 0:
                if prev <= 0:
                    prev = nums[i]
                else:
                    prev += nums[i]
            else:
                if prev >= 0:
                    prev += nums[i]
                else:
                    prev = nums[i]
        return max(prev, ans)

s = Solution()
print(s.maxSubArray([-2,1]))