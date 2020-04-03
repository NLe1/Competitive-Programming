"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        if len(nums) < 3: return []
        if len(nums) == 3: return [nums] if sum(nums) == 0 else []
        anchor, left, right = 0, 1, len(nums) - 1
        while right - anchor >= 2:
            while left < right:
                n1, n2, n3 = nums[anchor], nums[left], nums[right]
                curSum = n1 + n2 + n3
                if curSum == 0:
                    ans.append([n1, n2 ,n3])
                    while left < right and nums[left] == nums[left + 1]: left+=1
                    while left < right and nums[right] == nums[right - 1]: right+=1
                    left+=1
                    right-=1
                if curSum <= 0: left += 1
                else: right-=1
            while nums[anchor] == nums[anchor + 1] and len(nums) - anchor >= 3: anchor+=1
            left=anchor+1
            right=len(nums)-1
        return list(ans)

s = Solution()
print(s.threeSum([0,0,0,0]))
