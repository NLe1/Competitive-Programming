class Solution:
    def minPathSum(self, grid) -> int:
        ver = [grid[row][-1] for row in range(len(grid))]
        hor = grid[-1]
        for row in range(len(grid)):
            grid[row][-1] = sum(ver[row:])
        for col in range(len(grid[0])):
            grid[-1][col] = sum(hor[col:])
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[0]) - 2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))