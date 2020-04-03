class Solution:
    def expandAndCount(self, s, left, right):
        if s[left] != s[right]: return s[0]
        curLeft, curRight = left, right
        while curLeft - 1 >= 0 and curRight + 1<= len(s) - 1 and s[curLeft - 1] == s[curRight + 1]:
            curLeft -= 1
            curRight += 1

        return s[curLeft: curRight + 1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        m = ""
        for i in range(len(s)):
            single, double =self.expandAndCount(s, i, i), self.expandAndCount(s, i - 1, i)
            m = single if len(single) > len(m) else m
            m = double if len(double) > len(m) else m
        return m


s = Solution()
print(s.longestPalindrome("abb"))