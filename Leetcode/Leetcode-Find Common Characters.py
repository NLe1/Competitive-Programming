from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 1: return list(A[0])
        c = Counter(A[0])

        for i in range(1, len(A)):
            for ch in c.keys():
                if c[ch] > 0:
                    if A[i].count(ch) == 0:
                        c[ch] = 0
                        continue
                    if A[i].count(ch) < c[ch]: c[ch] = A[i].count(ch)
        ans = []
        for ch,n in c.items():
            for x in range(n): ans.append(str(ch))

        return ans