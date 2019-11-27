class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = [list("abcde"), list("fghij"),list("klmno"),list("pqrst"),list("uvwxy"),["z"]]
        d = {}
        for r,_ in enumerate(board):
            for c, ch in enumerate(_):
                d[ch] = (r,c)
        x1,y1=0,0
        ans = []
        for ch in target:
            x2,y2=d[ch]
            if x1 == x2 and y1 == y2:
                ans.append('!')
            else:
                v = x1-x2
                h = y1-y2
                if x1 == 5 and y1 == 0:
                    for i in range(abs(v)):
                        ans.append("U")
                    for i in range(abs(h)):
                        ans.append("R")
                    ans.append("!")
                elif x2 == 5 and y2 == 0:
                    for i in range(abs(h)):
                        ans.append("L")
                    for i in range(abs(v)):
                        ans.append("D")
                    ans.append("!")
                else:
                    if v > 0:
                        for i in range(abs(v)):
                            ans.append("U")
                    elif v < 0:
                        for i in range(abs(v)):
                            ans.append("D")
                    if h > 0:
                        for i in range(abs(h)):
                            ans.append("L")
                    elif h < 0:
                        for i in range(abs(h)):
                            ans.append("R")
                    ans.append("!")
            x1,y1=x2,y2
        return ''.join(ans)

s = Solution()
print(s.alphabetBoardPath("zeezz"))