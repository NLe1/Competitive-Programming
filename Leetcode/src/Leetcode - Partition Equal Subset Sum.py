class Solution:
    def canPartition(self, nums) -> bool:
        s = sum(nums)
        n = len(nums)
        if s & 1 == 1: return False

        target = int(s/2)

        dp = [[True for _ in range(target + 1)] if j > 0 else [False for _ in range(target + 1)] for j in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]

        for row in dp: print(row)
        return dp[n][target]

Solution().canPartition([1, 5, 11, 5])