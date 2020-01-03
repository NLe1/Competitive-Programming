import math
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        nums = set([n])
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n in nums:
                return False
            if n == 1:
                return True
            nums.add(n)

s = Solution()
print(s.isHappy(23242))