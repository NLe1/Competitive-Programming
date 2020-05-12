"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, N: int) -> int:
        d = {N: 1, N - 1: 1}
        def helper(n):
            nonlocal d
            if n in d: return d[n]
            else:
                ret = helper(n + 1) + helper(n + 2)
                d[n] = ret
                return ret
        return helper(0)

s = Solution()
print(s.climbStairs(4))