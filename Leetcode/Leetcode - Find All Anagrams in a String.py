import collections
class Solution:
    def isAnagram(self, dictP):
        return all([freq == 0 for freq in dictP.values()])

    def findAnagrams(self, s: str, p: str):
        ans = []
        dictS, dictP = collections.Counter(s[:len(p)]), collections.Counter(p)
        dictS.subtract(dictP)
        if self.isAnagram(dictS):
            ans.append(0)
        for i in range(1, len(s) - len(p) + 1):
            dictS[s[i-1]]-=1
            dictS[s[i+len(p)-1]]+=1
            if self.isAnagram(dictS):
                ans.append(i)
        return ans
s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))