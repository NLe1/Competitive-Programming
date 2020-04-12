"""
https://leetcode.com/problems/coin-change-2/

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""



def minAbs(nums):
    s = sum(nums) // 2
    n = len(nums)
    dp = [[0 for _ in range(s + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if nums[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], nums[i - 1] + dp[i - 1][j - nums[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    '''return second server loads - first server loads'''
    for row in dp:
        print(row)
    return (sum(nums) - dp[-1][-1]) - dp[-1][-1]

'''four testcases'''
print(minAbs([1, 2, 3, 4, 5]))
print(minAbs([10, 10, 9, 9, 2]))
print(minAbs([]))
print(minAbs([1]))