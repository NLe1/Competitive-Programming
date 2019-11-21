class Solution:
    def numTilings(self, N: int) -> int:
        p3,p2,p1 = -1,0,1
        cur = 0
        for i in range(N):
            cur = (2*p1+p3)
            p3 = p2
            p2 = p1
            p1 = cur
        return cur % (10 ** 9 + 7)

s = Solution()
print(s.numTilings(4))