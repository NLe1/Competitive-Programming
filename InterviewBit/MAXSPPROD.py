import collections


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        if A == sorted(A) or A == sorted(A, reverse=True) or len(A) <= 2: return 0
        d = collections.defaultdict(list)
        for i, item in enumerate(A):
            d[item].append(i)
        l = sorted(d.items(), reverse=True)
        l = [[item, sorted(d)] for item, d in l]
        m = 0
        start, end = 0, 0
        while end < len(l):
            if abs(l[start][1][0] - l[end][1][-1]) > 1 or abs(l[start][1][-1] - l[end][1][0]) > 1:
                m = max(m, l[start][0] * l[end][0])
                break
            end += 1

        if end - start > 1 and l[start + 1][0] * l[end - 1][0] > m and (
                abs(l[start + 1][1][0] - l[end - 1][1][-1]) > 1 or abs(l[start + 1][1][-1] - l[end - 1][1][0]) > 1):
            m = l[start + 1][0] * l[end - 1][0]
        return m

s = Solution()
print(s.maxSpecialProduct([ 7, 5, 7, 9, 8, 7 ]))
