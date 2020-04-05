class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        m, n = len(grid), len(grid[0])
        #directional vector
        dirs = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        def dfs(i, j):
            if  m - 1 < i or i < 0 or n - 1 < j or j < 0 or grid[i][j] != '1':
                return
            grid[i][j] = "*"
            for dirX, dirY in dirs:
                dfs(i + dirX, j + dirY)
            return
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        return count

print(Solution().numIslands([["1","1","1","1","0"],
                             ["1","1","0","1","0"],
                             ["1","1","0","0","0"],
                             ["0","0","0","0","0"]]))