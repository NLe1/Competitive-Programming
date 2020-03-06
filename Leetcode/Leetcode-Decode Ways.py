class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 0
        ct = 1
        for i in range(1, len(s)):
            if int(s[i-1] + s[i]) <= 26:
                ct *= 2
        return ct