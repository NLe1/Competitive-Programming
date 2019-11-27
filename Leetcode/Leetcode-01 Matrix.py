class Solution:
    def helper(self, visited, ans, countDone, ctr):
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                # if the current spot not zero
                if ans[i][j] == ctr:
                    if j - 1 >= 0 and ans[i][j - 1] > ctr + 1:
                        ans[i][j - 1] = ctr + 1
                        if not visited[i][j - 1]:
                            visited[i][j - 1] = True
                            countDone -= 1
                    if i - 1 >= 0 and ans[i - 1][j] > ctr + 1:
                        ans[i - 1][j] = ctr + 1
                        if not visited[i - 1][j]:
                            visited[i - 1][j] = True
                            countDone -= 1
                    if i + 1 <= len(ans) - 1 and ans[i + 1][j] > ctr + 1:
                        ans[i + 1][j] = ctr + 1
                        if not visited[i + 1][j]:
                            visited[i + 1][j] = True
                            countDone -= 1
                    if j + 1 <= len(ans[0])-1 and ans[i][j + 1] > ctr + 1:
                        ans[i][j + 1] = ctr + 1
                        if not visited[i][j + 1]:
                            visited[i][j + 1] = True
                            countDone -= 1
        return countDone

    def updateMatrix(self, matrix):
        ans = []
        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        countDone = len(matrix) * len(matrix[0])
        ctr = 0
        for x in range(len(matrix)):
            temp = []
            for y in range(len(matrix[0])):
                if not matrix[x][y]:
                    temp.append(0)
                    visited[x][y] = True
                    countDone -= 1
                else:
                    temp.append(10000)
            ans.append(temp)
        while countDone:
            countDone = self.helper(visited, ans, countDone, ctr)
            ctr += 1
        return ans


s = Solution()
print(s.updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                      [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))
