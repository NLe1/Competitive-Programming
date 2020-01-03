class Solution:
    # backtracking
    def exist(self, board, word: str) -> bool:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nRow = len(board)
        nCol = len(board[0])

        # ind is the index of the character of the word that currently seeking
        def dfs(i, j, ind):
            ch = board[i][j]
            if ch != word[ind]:
                return False

            if ind == len(word) - 1:
                return True

            board[i][j] = ''
            ret = any(
                dfs(i + I, j + J, ind + 1) for I, J in direction if 0 <= i + I <= nRow - 1 and 0 <= j + J <= nCol - 1)

            board[i][j] = ch

            return ret

        for i in range(nRow):
            for j in range(nCol):
                if dfs(i, j, 0):
                    return True
        return False
print(Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ASFDAS'))
