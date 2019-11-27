from collections import Counter

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        c1 = Counter(list(text1))
        c2 = Counter(list(text2))
        for ch in c2.keys():
            c1[ch] = max(c1.get(ch,0), c2[ch])
        ans = []
        i = 0
        while i < len(text1) and i < len(text2):
            ch1,ch2 = text1[i], text2[i]
            if c1[ch1] > 0:
                ans.append(ch1)
                c1[ch1]-=1
            if c1[ch2] > 0:
                ans.append(ch2)
                c1[ch2]-=1
            i+=1
        while i < len(text1):
            ch1 = text1[i]
            if c1[ch1] > 0:
                ans.append(ch1)
                c1[ch1] -= 1
            i+=1
        while i < len(text2):
            ch2 = text2[i]
            if c1[ch2] > 0:
                ans.append(ch2)
                c1[ch2] -= 1
            i+=1
        return "".join(ans)

s = Solution()
print(s.longestCommonSubsequence("abac"
                                 , "cab"))
