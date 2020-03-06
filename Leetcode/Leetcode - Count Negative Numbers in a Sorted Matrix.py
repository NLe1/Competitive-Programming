class Solution:
    def countNegatives(self, grid) -> int:
        ct = 0
        if not grid: return 0
        if grid[0][0] < 0: return len(grid) * len(grid[0])
        if grid[-1][-1] > 0: return 0
        stack = [(len(grid) - 1,len(grid[0])-1)]
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        while stack:
            i,j = stack.pop()
            visited[i][j] = True
            if grid[i][j] < 0: ct+=1
            if i-1>=0 and grid[i-1][j] < 0 and not visited[i-1][j]:
                stack.append((i-1,j))
            if j-1 >=0 and grid[i][j-1] < 0 and not visited[i][j-1]:
                stack.append((i,j-1))
        return ct

s=Solution()
print(s.countNegatives([[-1]]))