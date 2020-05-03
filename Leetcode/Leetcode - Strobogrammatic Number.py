"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 0: return True
        if len(num) % 2 == 1 and num[int(len(num) / 2)] not in '018': return False
        d = {'6':'9','9':'6','8':'8','1':'1','0':'0'}
        left, right = 0, len(num) - 1
        while left < right:
            if d[num[left]] != num[right]: return False
            left+=1
            right-=1
        return True

s = Solution()
print(s.isStrobogrammatic("10801"))