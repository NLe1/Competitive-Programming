"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    def maximalSquare(self, matrix: [[int]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return len(matrix) and max(max(row) for row in matrix) ** 2

s = Solution()
print(s.maximalSquare([
    [1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0]

]))