import itertools


class Solution:
    def longestWPI(self, hours) -> int:
        l = [1 if x > 8 else -1 for x in hours]
        s = list(itertools.accumulate(l))
        d = {}
        cur = 0
        for i, item in enumerate(s):
            if item > 0:
                cur = i + 1
            else:
                d[item - 1] = i
        for k, v in d.items():
            if k not in s:
                continue
            ind = s.index(k)
            cur = max(cur, v - ind)
        return cur


s = Solution()
print(s.longestWPI(
    [6, 9, 9]))
