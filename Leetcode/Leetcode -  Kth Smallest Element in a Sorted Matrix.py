"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
import math
class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        upper = int(math.sqrt(k - 1)) + 1
        lower = (upper - 1) ** 2
        nums = matrix[upper - 1][:upper] + [matrix[row][upper - 1] for row in range(upper - 1)]
        nums.sort()
        return nums[k - int(lower) - 1]
s = Solution()
print(s.kthSmallest([[1,3,5],
                     [6,7,12],
                     [11,14,14]],3))