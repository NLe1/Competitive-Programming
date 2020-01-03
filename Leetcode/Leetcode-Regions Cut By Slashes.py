import collections
class Solution:
    def regionsBySlashes(self, grid) -> int:
        m = [[0] * (len(grid[0]) * 3) for i in range(3 * len(grid))]
        for i,r in enumerate(grid):
            for j,c in enumerate(list(r)):
                startX, startY= 3 * i, 3 * j
                if c == '/':
                    m[startX + 2][startY], m[startX + 1][startY + 1], m[startX][startY + 2]= 1,1,1
                elif c == '\\':
                    m[startX][startY], m[startX + 1][startY + 1], m[startX + 2][startY + 2]= 1,1,1

        count = 0
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] == 0:
                    count += 1
                    #flooding
                    stack = [(i,j)]
                    while stack:
                        x,y = stack.pop()
                        m[x][y] = 1
                        if x - 1 >= 0 and m[x-1][y] == 0:
                            stack.append((x-1,y))
                        if y - 1 >= 0 and m[x][y-1] == 0:
                            stack.append((x,y-1))
                        if x + 1 <= len(m) - 1 and m[x+1][y] == 0:
                            stack.append((x+1,y))
                        if y + 1 <= len(m) - 1 and m[x][y + 1] == 0:
                            stack.append((x,y + 1))
        return count




print(Solution().regionsBySlashes(["//",
  "/ "]))