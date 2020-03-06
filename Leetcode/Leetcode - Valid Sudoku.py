import collections

class Solution:
    def isValidSudoku(self, board) -> bool:
        d = collections.defaultdict(set)
        for r,row in enumerate(board):
            for c, col in enumerate(row):
                if col == '.':
                    continue
                if col in d[f'r_{r}'] or col in d[f'c_{c}'] or col in d[f'b_{r//3}_{c//3}']:
                    return False
                d[f'r_{r}'].add(col)
                d[f'c_{c}'].add(col)
                d[f'b_{r // 3}_{c // 3}'].add(col)
        return True

print(Solution().isValidSudoku(
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
))