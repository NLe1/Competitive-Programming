class Solution:
    def countNeighbors(self, curX, curY, board):
        ct = 0
        if curX + 1 <= len(board) - 1:
            ct += board[curX + 1][curY]
            if curY + 1 <= len(board[0]) - 1:
                ct += board[curX + 1][curY + 1]
        if curX - 1 >= 0:
            ct += board[curX - 1][curY]
            if curY - 1 >= 0:
                ct += board[curX - 1][curY - 1]
        if curY + 1 <= len(board[0]) - 1:
            ct += board[curX][curY + 1]
            if curX - 1 >= 0:
                ct += board[curX - 1][curY + 1]
        if curY - 1 >= 0:
            ct += board[curX][curY - 1]
            if curX + 1 <= len(board) - 1:
                ct += board[curX + 1][curY - 1]
        return ct

    def gameOfLife(self, board) -> None:
        temp = []
        for x,r in enumerate(board):
            ph = []
            for y,num in enumerate(r):
                #if 0, look for the total live neighbor
                if num == 0:
                    if self.countNeighbors(x, y, board) == 3:
                        ph.append(1)
                    else:
                        ph.append(0)
                else:
                    if 2 <= self.countNeighbors(x,y,board) <= 3:
                        ph.append(1)
                    else:
                        ph.append(0)
            temp.append(ph)

        for x,r in enumerate(temp):
            for y, c in enumerate(r):
                board[x][y] = c

m = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]
Solution().gameOfLife(m)
print(m)