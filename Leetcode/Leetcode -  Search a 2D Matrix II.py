"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution:
    def searchMatrix(self, matrix, target, lowerX = 0, lowerY= 0):
        if not matrix or not matrix[0]: return False
        M,N = len(matrix), len(matrix[0])
        curX, curY = 0, N - 1
        while curX <= M - 1 and curY >= 0:
            if matrix[curX][curY] == target: return True
            elif matrix[curX][curY] < target: curX += 1
            else: curY -= 1
        return False

s = Solution()
print(s.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
20))