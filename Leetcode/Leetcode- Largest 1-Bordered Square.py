class Solution:
    def helper(self, anI, anJ, di, grid):
        for m in range(di, -1, -1):
            if all(grid[anI + k][anJ] for k in range(m + 1)) and all(
                    grid[anI + k][anJ + m] for k in range(m + 1)) and all(
                grid[anI][anJ + k] for k in range(m + 1)) and all(
                grid[anI + m][anJ + k] for k in range(m + 1)):
                return (m + 1) ** 2
        return 1

    def largest1BorderedSquare(self, grid) -> int:
        H = len(grid[0]) - 1
        V = len(grid) - 1
        ans = 0
        for i in range(V + 1):
            for j in range(H + 1):
                # for each position that is not 0
                if grid[i][j]:
                    mH = H - j
                    mV = V - i
                    an = self.helper(i, j, min(mH, mV), grid)
                    ans = an if an > ans else ans
        return ans


s = Solution()
print(s.largest1BorderedSquare([[0, 1, 1, 1],
                                [1, 1, 1, 1],
                                [1, 0, 0, 1],
                                [1, 1, 1, 1],
                                [1, 0, 1, 1],
                                [1, 1, 0, 1]]))
