from collections import defaultdict
class Solution:
    def minAreaRect(self, points) -> int:
        if len(points) <= 3: return 0
        x= defaultdict(set)
        for xC, yC in points:
            x[xC].add(yC)
        m = float('inf')
        for p1 in points:
            for p2 in points:
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                else:
                    if p2[1] in x[p1[0]] and p1[1] in x[p2[0]]:
                        t = abs(p1[0] - p2[0]) * abs(p1[1]-p2[1])
                        m = min(t,m)
        return m if m < float('inf') else 0

s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))