"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) * len(b) == 0: return a + b
        a = a[::-1]
        b = b[::-1]
        c = '0'
        ans = []
        lesserLength = min(len(a), len(b))
        for i in range(lesserLength):
            if a[i] == b[i]:
                ans.append(c)
                c = a[i]
            else:
                if c == '1':
                    ans.append('0')
                else:
                    ans.append('1')
        for i in range(lesserLength, len(a)):
            if c == '1':
                if a[i] == '1':
                    ans.append('0')
                else:
                    ans.append('1')
                    c = '0'
            else:
                ans.append(c)
                ans.append(a[lesserLength +1 :])
                break
        for i in range(lesserLength, len(b)):
            if c == '1':
                if b[i] == '1':
                    ans.append('0')
                else:
                    ans.append('1')
                    c = '0'
            else:
                ans.append(c)
                ans.append(b[lesserLength +1 :])
                break
        ans.append(c)
        ans = ''.join(ans[::-1]).lstrip('0')
        return '0' if len(ans) == 0 else ans
s = Solution()
print(s.addBinary("0", "0"))