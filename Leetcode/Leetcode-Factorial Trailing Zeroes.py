import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        return int(n / 5) + self.trailingZeroes(int(n / 5))

s = Solution()
n = 30
print(math.factorial(n))
print(s.trailingZeroes(n))
