class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        s = list(s)
        s.reverse()
        t = list(t)
        t.reverse()

        for i in range(len(t)):
            if t[i] == s[0]: s.pop(0)
            if len(s) == 0: break

        if len(s) > 0:
            return False
        else:
            return True