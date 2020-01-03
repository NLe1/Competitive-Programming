class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        matrix[:] = matrix[::-1]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] = matrix[j][i]

s = Solution()
print(s.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
