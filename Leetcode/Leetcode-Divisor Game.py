import math
class Solution:
    # whether Alice will win at N (key) when her turn
    aTable = {2: True, 3: False, 1: False}
    # whether Alice will win at N (key) when opponent turn
    nTable = {2: False, 3: True, 1: True}
    def getRes(self, N, turn):
        if turn and N in self.aTable: return self.aTable.get(N)
        if not turn and N in self.nTable: return self.nTable.get(N)
        win = None
        divisor = []
        for i in range(1, int(math.sqrt(N)) + 1):
            if N % i == 0:
                divisor.append(i)
                if i != 1 and i != N / i:
                    divisor.append(int(N/i))
        divisor.sort(reverse=True)
        if turn:
            win = any(self.getRes(N - x, not turn) for x in divisor)
            self.aTable[N] = win
            return win
        else:
            win = all(self.getRes(N - x, not turn) for x in divisor)
            self.nTable[N] = win
            return win

    def divisorGame(self, N: int) -> bool:
        return self.getRes(N, True)