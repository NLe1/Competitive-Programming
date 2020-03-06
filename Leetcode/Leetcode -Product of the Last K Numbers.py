import collections
import bisect
class ProductOfNumbers:

    def __init__(self):
        self.curMax = (0,0,0) #(k, value, count)
        self.list = []
        self.count = 0

    def add(self, num: int) -> None:
        self.list.append(num)
        self.count += 1

    def getProduct(self, k: int) -> int:
        if self.curMax == (0,0,0):
            cur = len(self.list) - 1
            res = 1
            for i in range(k):
                res *= self.list[cur - i]
            self.curMax = (k, res, self.count)
            return res
        else:
            lastK, lastValue, lastCount = self.curMax
            curValue, curK = 1, k
            for i in range(self.count - lastCount):
                curValue *= self.list[-1-i]
                curK -= 1
                if curK == 0:
                    return curValue
            if curK >= lastK:
                curValue *= lastValue
                if curValue == 0:
                    return 0
                for i in range(curK - lastK):
                    curValue *= self.list[lastCount - lastK - 1 - i]
            else:
                for i in range(curK):
                    curValue *= self.list[ -1 - self.count + lastCount - i]

            if k >= lastK and curValue != 0:
                self.curMax = (k, curValue, self.count)
            return curValue


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)        # [3,0,2,5]
productOfNumbers.add(4)        # [3,0,2,5,4]
print(productOfNumbers.getProduct(2)) # return 20. The product of the last 2 numbers is 5 * 4 = 20
print(productOfNumbers.getProduct(3)) # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(productOfNumbers.getProduct(4)) # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)        # [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2))