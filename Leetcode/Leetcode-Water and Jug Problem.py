import math
class Solution:
    def canMeasureWater(self, X: int, Y: int, Z: int) -> bool:
        return False if Z > X + Y else True if Z % math.gcd(X,Y) == 0 else False


s = Solution()
print(s.canMeasureWater(2,
                        6,
                        4))
