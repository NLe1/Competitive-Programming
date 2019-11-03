class Solution:
    INT_MAX = 2**31-1
    INT_MIN = -2**31
    def divide(self, dividend: int, divisor: int) -> int:
        n = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            n = True
        if divisor == 1 and self.INT_MIN <= dividend <= self.INT_MAX:
            if n:
                return -abs(dividend)
            else:
                return abs(dividend)
        divisor = abs(divisor)
        dividend = abs(dividend)

        if divisor == 1 and (dividend > self.INT_MAX or dividend < self.INT_MIN):
            return self.INT_MAX
        if abs(dividend) < abs(divisor):
            return 0

        i = 1
        ans = 0
        val = 0

        while True:
            if dividend >= val + divisor ** i:
                ans += divisor ** (i - 1)
                val += divisor ** i
            else:
                ans += self.divide(dividend - val, divisor)
                if n: ans = -ans
                if n < self.INT_MIN or n > self.INT_MAX:
                    return self.INT_MAX
                else:
                    return ans
            i += 1