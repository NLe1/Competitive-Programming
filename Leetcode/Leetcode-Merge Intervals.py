import bisect
class Solution:
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18], [0,7]]))
