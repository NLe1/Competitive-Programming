import math


class Solution:
    def primeFactors(self, n):
        ct = 0
        while n % 2 == 0:
            ct += 2
            n /= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                ct += i
                n = n / i
        if n > 2:
            ct += int(n)
        return ct

    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        return self.primeFactors(n)


s = Solution()
print(s.minSteps(1000))
