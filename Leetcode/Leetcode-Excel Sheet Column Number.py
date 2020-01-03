import math
class Solution:
    def titleToNumber(self, s: str) -> int:
        st = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans,l = 0, len(s)
        for i in range(l, 0, -1):
            ans += 26 ** (i-1) * (st.index(s[l-i]) + 1)
        return ans
s = Solution()
print(s.titleToNumber("ZY"))