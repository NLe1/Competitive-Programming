"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

import math
class NumArray:
    def __init__(self, nums: [int]):
        if nums:
            self.nums = nums
            lenTrees = 2 ** (math.ceil(math.log(len(nums), 2)) + 1) - 1
            print(lenTrees)
            self.trees = [0] * lenTrees
            self.buildTrees(0, len(nums) - 1, 0)

    def buildTrees(self, lo, hi, index):
        if lo == hi:
            self.trees[index] = self.nums[lo]
            return self.trees[index]
        mid = lo + int((hi - lo) / 2)
        left = self.buildTrees(lo, mid, index * 2 + 1)
        right=self.buildTrees(mid + 1, hi, index * 2 + 2)
        self.trees[index] = left + right
        return self.trees[index]

    def sumRange(self, i: int, j: int) -> int:
        def querySumRange(lo, hi, index):
            nonlocal i,j
            if hi < i or lo > j: return 0
            if i <= lo <= hi <= j: return self.trees[index]
            mid = lo + int((hi - lo) / 2)
            if mid < i:
                return querySumRange(mid + 1, hi, index * 2 + 2)
            if mid > j:
                return querySumRange(lo, mid, index * 2 + 1)
            return querySumRange(mid + 1, hi, index * 2 + 2) + querySumRange(lo, mid, index * 2 + 1)
        return querySumRange(0, len(self.nums) - 1, 0)


s = NumArray([-2, 0, 3, -5, 2, -1])
print(s.sumRange(2,3))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

