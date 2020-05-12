"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex:int) -> [int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        ans = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            prev, next = 1, 1
            for j in range(1, i):
                next = ans[j] + prev
                prev = ans[j]
                ans[j] = next
        return ans

s = Solution()
print(s.getRow(5))