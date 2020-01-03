class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for ch in s:
            if ch.isalnum():
                l.append(ch.lower())
        print(l)
        return list(reversed(l)) == l

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))