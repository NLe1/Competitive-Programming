class Solution:
    def reverseBits(self, n: int) -> int:
        s = "{0:b}".format(n)
        s = "0" * (32 - len(s)) + s
        print(s)
        return int(s[::-1], 2)


s = Solution()
print(s.reverseBits(4294967293))
