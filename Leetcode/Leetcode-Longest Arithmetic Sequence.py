class Solution:
    def longestArithSeqLength(self, A) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        print(dp)
        return max(dp.values())
