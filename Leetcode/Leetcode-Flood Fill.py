class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        q = [[sr, sc]]
        old = image[sr][sc]
        while len(q) > 0:
            curR,curC = q.pop()
            image[curR][curC] = newColor
            visited[curR][curC] = True
            if curR-1>=0 and image[curR-1][curC] == old and not visited[curR-1][curC]:
                q.append([curR-1, curC])
            if curR+1<=len(image)-1 and image[curR+1][curC] == old and not visited[curR+1][curC]:
                q.append([curR+1, curC])
            if curC-1>=0 and image[curR][curC-1] == old and not visited[curR][curC-1]:
                q.append([curR, curC-1])
            if curC+1<=len(image[0])-1 and image[curR][curC+1] == old and not visited[curR][curC+1]:
                q.append([curR, curC+1])
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))