class Solution:
    def getFlipEven(self, n):
        ans = 0
        for i in range(n - 2, -1, -2):
            ans += 2 ** i
        return ans

    def getFlipOdd(self, n):
        ans = 0
        for i in range(n - 1, -1, -2):
            ans += 2 ** i
        return ans

    def getFlipAll(self, n):
        return 2 ** n - 1

    def getFlip3k(self, n):
        ans = 0
        for i in range(n - 1, -1, -3):
            ans += 2 ** i
        return ans

    def flipLights(self, n: int, m: int) -> int:
        if m == 0: return 1
        start = self.getFlipAll(n)
        e, o, a, t = self.getFlipEven(n), self.getFlipOdd(n), self.getFlipAll(n), self.getFlip3k(n)
        ans = set()
        if m == 1:
            ans.add(start ^ e)
            ans.add(start ^ o)
            ans.add(start ^ a)
            ans.add(start ^ t)
        elif m == 2:
            ans.add(start)
            ans.add(start ^ e ^ o)
            ans.add(start ^ e ^ a)
            ans.add(start ^ e ^ t)
            ans.add(start ^ o ^ a)
            ans.add(start ^ o ^ t)
            ans.add(start ^ a ^ t)
        else:
            if m % 2 == 0 and m > 2:
                ans.add(start)
                ans.add(start ^ e ^ o ^ a ^ t)
                ans.add(start ^ e ^ o)
                ans.add(start ^ e ^ a)
                ans.add(start ^ e ^ t)
                ans.add(start ^ o ^ a)
                ans.add(start ^ o ^ t)
                ans.add(start ^ a ^ t)
            elif m % 2 == 1 and m > 1:
                ans.add(start ^ e)
                ans.add(start ^ o)
                ans.add(start ^ a)
                ans.add(start ^ t)
                ans.add(start ^ e ^ o ^ a)
                ans.add(start ^ e ^ o ^ t)
                ans.add(start ^ e ^ a ^ t)
                ans.add(start ^ o ^ a ^ t)
        return len(ans)

s = Solution()
print(s.flipLights(3,1))
