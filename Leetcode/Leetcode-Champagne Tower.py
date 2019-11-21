class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        res = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                r = max(res[i] - 1, 0) / 2.0
                l = max(res[i - 1] - 1, 0) / 2.0
                res[i] = r+l
        return min(res[query_glass], 1)


s = Solution()
print(s.champagneTower(100000000, 99, 45))
