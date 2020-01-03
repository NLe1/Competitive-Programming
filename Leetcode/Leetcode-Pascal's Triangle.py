class Solution:
    def generate(self, numRows: int):
        if not numRows: return []
        if numRows == 1: return[[1]]
        if numRows == 2: return[[1],[1,1]]
        ans = [[1], [1,1]]
        for i in range(2, numRows):
            temp = [1] * (i + 1)
            for j in range(1, len(ans[i-1])):
                temp[j] = ans[i-1][j] + ans[i-1][j-1]
            ans.append(temp)
        return ans
s = Solution()
for row in s.generate(100):
    print(row)
