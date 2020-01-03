class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans = "1"
        for i in range(2, n + 1):
            prev, ct = ans[0], 0
            nAns = []
            for ch in ans:
                if ch == prev:
                    ct += 1
                else:
                    nAns.append(str(ct))
                    nAns.append(prev)
                    prev, ct = ch, 1
            nAns.append(str(ct))
            nAns.append(prev)
            ans = ''.join(nAns)
        return ans

s = Solution()
print(s.countAndSay(30))