from collections import defaultdict
import itertools
import bisect

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ind, d = 0, defaultdict(list)
        for ch in s:
            d[ch].append(ind)
            ind += 1
        m = 0
        for ch, l in d.items():
            pr = [l[i] - l[i - 1] - 1 for i in range(1, len(l))]
            pr = list(itertools.accumulate(pr))
            if not len(pr):
                m = max(1 + k, m)
            else:
                for j in range(len(l)-1):
                    start = 0 if j == 0 else pr[j - 1]
                    left = k + start
                    ct = 1
                    ind = bisect.bisect_right(pr, left)
                    ct = k + ind - j + 1
                    m = max(ct, m)
        return m

s = Solution()
print(s.characterReplacement("AABABBA", 1))
