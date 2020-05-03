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
    def maximalSquare(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if i * j > 0 and matrix[i][j] != 0:
                    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j])
        return int(max([max(row) for row in matrix]) ** 2)

s = Solution()
print(s.maximalSquare([["1","0","1","0"],
                       ["1","0","1","1"],
                       ["1","0","1","1"],
                       ["1","1","1","1"]]))