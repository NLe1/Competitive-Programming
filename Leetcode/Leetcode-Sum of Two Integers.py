class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a if b == 0 else self.getSum(a ^ b, (a & b) << 1)

s = Solution()
print(s.getSum(23423,-2398423))
