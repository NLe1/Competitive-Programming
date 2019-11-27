class Solution:
    def getNextNumber(self, s, i):
        temp = [s[i]]
        while i + 1 < len(s):
            if s[i + 1].isnumeric():
                temp.append(s[i + 1])
                i += 1
            else:
                break
        return ''.join(temp)

    def calculate(self, s: str) -> int:
        s = list(s.strip())
        for x in range(s.count(' ')):
            s.remove(' ')
        nStack = []
        opStack = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                number = self.getNextNumber(s, i)
                nStack.append(number)
                i += len(number)
            else:
                if s[i] == '*':
                    first, second = float(nStack.pop()), self.getNextNumber(s, i + 1)
                    nStack.append(first * float(second))
                    i += len(second)
                elif s[i] == '/':
                    first, second = float(nStack.pop()), self.getNextNumber(s, i + 1)
                    nStack.append(int(first / float(second)))
                    i += len(second)
                else:
                    opStack.append(s[i])
                i+=1
        while len(opStack) > 0:
            op = opStack.pop(0)
            if op == '+':
                first, second = float(nStack.pop(0)), float(nStack.pop(0))
                nStack.insert(0,first + second)
            else:
                first, second = float(nStack.pop(0)), float(nStack.pop(0))
                nStack.append(0,first - second)
        return int(nStack[0])


s = Solution()
print(s.calculate("1+1-1"))
