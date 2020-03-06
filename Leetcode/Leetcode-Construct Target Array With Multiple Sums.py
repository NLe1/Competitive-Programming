class Solution:
    def isPossible(self, target) -> bool:
        while True:
            maxNum, maxIndex = float("-inf"), 0
            for i, num in enumerate(target):
                if num > maxNum:
                    maxNum = num
                    maxIndex = i
            total = sum(target)
            if total == len(target):
                return True
            sub = 2 * maxNum - total
            if  sub <= 0: return False
            target[maxIndex] = sub

s = Solution()
print(s.isPossible([8,5]))