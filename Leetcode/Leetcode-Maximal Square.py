
"""
O(m*n) but a bit slower more verbose
"""
class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix: return 0
        if min(len(matrix), len(matrix[0])) < 2: return 1 if any(any(int(col) for col in row) for row in matrix) else 0
        ret, cUp, cLeft = [[int(col) for col in row] for row in matrix],[[0]*len(matrix[0]) for i in range(len(matrix) + 1)],[[0]*len(matrix[0]) for i in range(len(matrix) +1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cUp[i][j] = ret[i][j] + cUp[i-1][j] if ret[i][j] == 1 else 0
                cLeft[i][j] = ret[i][j] + cLeft[i][j-1] if ret[i][j] == 1 else 0

        #start at the row and col index 1:
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                ret[i][j] = min(ret[i-1][j-1] + 1, min(cLeft[i][j], cUp[i][j]))
        return max(max(row) for row in ret) ** 2

"""
much shorter O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return len(matrix) and max(max(row) for row in matrix) ** 2
"""