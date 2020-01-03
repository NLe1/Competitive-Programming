from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals):
        index, d , ans= dict(), dict(),[]
        for i,[start, end] in enumerate(intervals):
            index[(start, end)] = i
            d[start] = end
        m, so = max(d.keys()), sorted(d.keys())
        for start, end in intervals:
            if end > m: ans.append(-1)
            else:
                ind = bisect_left(so, end)
                ans.append(index[(so[ind], d[so[ind]])])
        return ans

s = Solution()
print(s.findRightInterval([ [3,4], [2,3], [1,2] ]))

