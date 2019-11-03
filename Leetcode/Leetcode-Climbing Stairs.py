class Solution:
    def cal(self, n, d):
        if n in d.keys(): return d[n]
        if n == 1: return 1
        if n == 2: return 2

        # ways to climb n stairs equal to ways to climb on n-1 stairs and n-2 stairs
        ways = self.cal(n - 1, d) + self.cal(n - 2, d)
        d[n] = ways
        return ways

    def climbStairs(self, n: int) -> int:
        return self.cal(n, dict())
