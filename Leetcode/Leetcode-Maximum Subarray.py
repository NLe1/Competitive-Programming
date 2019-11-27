import itertools


class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i])
        print(dp)
        return max(dp)


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
