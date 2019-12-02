from collections import defaultdict
from bisect import bisect_left
## this is deformed of LCS problem

class Solution:
    def helper(self, index, cur, d1, d2, B):
        # if out of bound
        if index == len(B):
            return 0
        num = B[index]
        # if can not connect to any further point
        nextCurInd = bisect_left(d1[num], cur)
        if num not in d1 or nextCurInd == len(d1[num]):
            d2[(index, cur)] = self.helper(index + 1, cur, d1, d2, B)
            return d2[(index, cur)]
        # if memoized
        if (index, cur) in d2:
            return d2[(index, cur)]

        d2[(index, cur)] = max(self.helper(index + 1, cur, d1, d2, B),
                                               1 + self.helper(index + 1, d1[num][nextCurInd] + 1, d1, d2, B))
        return d2[(index, cur)]

    def maxUncrossedLines(self, A, B) -> int:
        if len(A) == 1 or len(B) == 1:
            if A[0] in B or B[0] in A:
                return 1
            else:
                return 0
        d1 = defaultdict(list)
        for i, n in enumerate(A):
            d1[n].append(i)
        d2 = {}
        m = max(self.helper(0, 0, d1, d2, B), self.helper(1, 0, d1, d2, B))
        print(d1)
        print(d2)
        return m


s = Solution()
print(s.maxUncrossedLines(
    [4, 1, 2, 5, 1, 5, 3, 4, 1, 5],
    [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]))
