"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

from collections import deque
class Solution:
    def findStrobogrammatic(self, n: int) -> [str]:
        if n == 0: return []
        if n == 1: return ["1", "0", "8"]
        outerPair, evenPair, ans, base = [("1","1"),("6","9"),("9","6"),("8","8")],[("1","1"),("6","9"),("0","0"),("9","6"),("8","8")], [], [(deque(""), 0)] #queue and curLength
        if n % 2 == 1:
            base = deque()
            for item in ["1", "0", "8"]:
                base.append((deque(item), 1))
        else: base = deque(base)
        while len(base) > 0:
            curBase, curLength = base.popleft()
            curBase = list(curBase)
            curLength += 2
            if curLength == n:
                curSeq = "".join(list(curBase))
                for head, tail in outerPair:
                    ans.append(head + curSeq + tail)
            else:
                for head, tail in evenPair:
                    newBase = deque(curBase)
                    newBase.appendleft(head)
                    newBase.append(tail)
                    base.append((newBase, curLength))
        return ans
s = Solution()
print(s.findStrobogrammatic(10))