class Solution:
    def getNextState(self, c):
        if c == '9': return ['0','8']
        if c == '8': return ['9','7']
        if c == '7': return ['8','6']
        if c == '6': return ['7','5']
        if c == '5': return ['6','4']
        if c == '4': return ['5','3']
        if c == '3': return ['4','2']
        if c == '2': return ['3','1']
        if c == '1': return ['2','0']
        if c == '0': return ['1','9']

    def openLock(self, deadends, target: str) -> int:
        if '0000' in deadends: return -1
        d = {target:0}
        for item in deadends:
            d[item] = -1
        q = [[target,0]]
        while len(q) > 0:
            item, cost = q.pop(0)
            if item in d.keys():
                if d[item] != -1 and d[item] > cost:
                    d[item] = cost
                    continue
                if d[item] == -1:
                    continue
            for i in range(len(item)):
                for rep in self.getNextState(item[i]):
                    new = item[:i]+rep+item[i+1:]
                    if new in d.keys():
                        if cost+1<d[new]:
                            d[new] = cost+1
                    else:
                        d[new] = cost+1
                        q.append([new, cost+1])
        if '0000' not in d: return -1
        return d['0000']

s = Solution()
print(s.openLock(["0000"], "8888"))