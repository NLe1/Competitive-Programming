from collections import Counter
import random
import sys
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        s = list(S)
        ctZ, ctO = [], []
        cZ, cO = 0, 0
        c = Counter(s)
        for i in range(len(s)):
            if s[i] == '0':
                cZ += 1
            if s[i] == '1':
                cO += 1
            ctZ.append(cZ)
            ctO.append(cO)
        min = sys.maxsize
        for i in range(0, len(s) + 1):
            l = ctO[i - 1] if i - 1 >= 0 else 0
            r = c['0'] - ctZ[i - 1] if i - 1 >= 0 else c['0']
            if r + l < min: min = r + l
        return min


s = Solution()
st = []
for i in range(20001):
    st.append(str(random.randint(0,1)))

print(s.minFlipsMonoIncr("".join(st)))