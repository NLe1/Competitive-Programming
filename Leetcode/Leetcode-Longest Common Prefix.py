class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        l = len(strs)
        if strs == []:
            return ""
        if l == 1:
            return strs[0]
        if strs[0] == "": return ""

        for j in range(0, min(len(strs[0]), len(strs[1]))):
            if strs[0][j] == strs[1][j]:
                s += strs[0][j]
            else:
                break

        for i in range(2, l):
            if s in strs[i] and strs[i].index(s) == 0: continue
            s = s[:-1]
            while s not in strs[i] or strs[i].index(s) != 0:
                if s == "" : return ""
                s = s[:-1]

        return s