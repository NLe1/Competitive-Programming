import collections
class Solution:
    def fourSumCount(self, A,B,C,D) -> int:
        dAB, dCD = collections.defaultdict(lambda: 0), collections.defaultdict(lambda: 0)
        for a in A:
            for b in B:
                dAB[a + b] += 1
        for c in C:
            for d in D:
                dCD[c + d] += 1
        print(dAB, dCD)
        ans = 0
        for k in dAB.keys():
            ans += dAB[k] * dCD[-k]

        return ans
s = Solution()
print(s.fourSumCount(
[-1,-1],
[-1,1],
[-1,1],
[1,-1],
))