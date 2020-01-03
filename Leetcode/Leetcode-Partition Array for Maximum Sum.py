def maxSumAfterPartitioning( A, K):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(N):
        curMax = 0
        for k in range(1, min(K, i + 1) + 1):
            curMax = max(curMax, A[i - k + 1])
            dp[i] = max(dp[i], dp[i - k] + curMax * k)
    return dp[N - 1]

print(maxSumAfterPartitioning([1,15,7,9,2,5,10],3))