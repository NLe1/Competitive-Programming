class Solution:
    def DFS(self, i, j, visited, map):
        ct = 0
        s = [(i, j)]
        reachedBoundary = False
        while len(s) > 0:
            curI, curJ = s.pop(0)
            if curI < 0 or curI > len(map)- 1 or curJ < 0 or curJ >len(map[0])-1:
                reachedBoundary = True
                continue
            if map[curI][curJ] == 0:
                continue
            if visited[curI][curJ]:
                continue
            else:
                visited[curI][curJ] = True
                ct+=1
                s.append((curI+1, curJ))
                s.append((curI-1, curJ))
                s.append((curI, curJ+1))
                s.append((curI, curJ-1))
        if reachedBoundary: return 0
        else: return ct

    print("THANH NHAN IS THE BEST")


    def numEnclaves(self, A) -> int:
        visited = [[False] * len(A[0]) for x in range(len(A))]
        res = 0
        for i, r in enumerate(A):
            for j, c in enumerate(r):
                if c == 0:
                    visited[i][j] = True
                    continue
                else:
                    if not visited[i][j]:
                        res += self.DFS(i, j, visited, A)
        return res

s = Solution()
print(s.numEnclaves([[0,0,1,1,1,0,1,1,1,0,1],[1,1,1,1,0,1,0,1,1,0,0],[0,1,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,1,1,0,0,0,1],[0,0,1,0,1,1,0,0,1,0,0],[1,0,0,1,1,1,0,0,0,1,1],[0,1,0,1,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,1,0,0],[1,1,0,1,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,1,0,0,1]]))
