class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        blRow, blCol = set(), set()
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    blRow.add(i)
                    blCol.add(j)
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if i in blRow or j in blCol:
                    matrix[i][j] = 0