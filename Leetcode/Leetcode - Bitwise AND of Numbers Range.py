"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""
import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m* n == 0: return 0
        strM = "{0:b}".format(m)
        strN = "{0:b}".format(n)
        if len(strM) < len(strN): strM = "0" * (len(strN) - len(strM)) + strM
        if len(strN) < len(strM): strN = "0" * (len(strM) - len(strN)) + strN

        ans = ["0"] * max(len(strM), len(strN))
        for i in  range(len(ans)):
            if strM[i] != strN[i]: break
            else: ans[i] = strM[i]
        return int(''.join(ans), 2)

s = Solution()
print(s.rangeBitwiseAnd(1,2))