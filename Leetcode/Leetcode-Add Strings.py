class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        cur = 0
        car = 0
        ans = []
        while cur < min(len(num1), len(num2)):
            ns = int(num1[cur]) + int(num2[cur]) + car
            car, nA = int(ns/10), ns%10
            ans.append(str(nA))
            cur+=1
        while cur < len(num1):
            ns = int(num1[cur]) + car
            car, nA = int(ns / 10), ns % 10
            ans.append(str(nA))
            cur+=1
        while cur < len(num2):
            ns = int(num2[cur]) + car
            car, nA = int(ns / 10), ns % 10
            ans.append(str(nA))
            cur+=1
        if car:
            ans.append("1")
        ans.reverse()
        return "".join(ans)

s = Solution()
print(s.addStrings("9923","232"))