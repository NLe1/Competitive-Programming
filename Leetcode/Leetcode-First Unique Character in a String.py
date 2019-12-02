from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(list(s))
        for i,ch in enumerate(list(s)):
            if c[ch] == 1:
                return i
        return -1

s =Solution()
print(s.firstUniqChar("loveleetcode"))