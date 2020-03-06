class Solution:
    def spiralOrder(self, matrix):
        if not len(matrix): return []
        if not len(matrix[0]): return []
        # if either has only 1 row or 1 column
        if len(matrix) == 1 or len(matrix[0]) == 1:
            if len(matrix) == 1: return matrix[0]
            else: return [row[0] for row in matrix]
        # if there are only 2 rows
        if len(matrix) == 2:
            secondList = matrix[1][::-1]
            return self.spiralOrder([matrix[0][:]]) + self.spiralOrder([secondList])

        # row > 2 && col > 1
        ret = matrix[0][:]
        ret.extend([row[-1] for i,row in enumerate(matrix) if 0 < i < len(matrix)])
        ret.extend(matrix[-1][:-1][::-1])
        ret.extend([row[0] for i,row in enumerate(matrix) if 0 < i < len(matrix) - 1][::-1])
        return ret + self.spiralOrder(
            [
                row[1: -1] for i, row in enumerate(matrix) if 0 < i < len(matrix) - 1
            ]
        )

s = Solution()
print(s.spiralOrder(
    [[1, 11],
     [2, 12],
     [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]
))

