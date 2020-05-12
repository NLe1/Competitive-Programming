"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

import math
class NumArray:

    def __init__(self, nums: [int]):
        if nums:
            lenNums = len(nums)
            segmentTreeLength = 2 ** int(math.ceil(math.log(lenNums, 2)) + 1) - 1
            self.trees = [0] * (segmentTreeLength)
            self.nums = nums
            self.buildTree(0, len(self.nums) - 1, 0)

    def buildTree(self, lower, upper, treesIndex):
        if lower == upper:
            self.trees[treesIndex] = self.nums[lower]
            return self.trees[treesIndex]

        middle = lower + int((upper - lower) / 2)
        left,right = self.buildTree(lower, middle, treesIndex * 2 + 1), self.buildTree(middle + 1, upper, treesIndex * 2 + 2)
        self.trees[treesIndex] = left + right
        return self.trees[treesIndex]

    def update(self, i: int, val: int) -> None:
        def updateTree(lower = 0, upper = len(self.nums) - 1, treesIndex = 0):
            nonlocal i, val
            if lower == upper == i:
                self.nums[i] = val
                oldVal, self.trees[treesIndex] = self.trees[treesIndex], val
                return val - oldVal

            changed, middle = 0, lower + int((upper - lower) / 2)
            if i > middle:
                changed =updateTree(middle + 1, upper, treesIndex * 2 + 2)
            else:
                changed = updateTree(lower, middle, treesIndex * 2 + 1)
            self.trees[treesIndex] += changed
            return changed
        return updateTree()

    def sumRange(self, i: int, j: int) -> int:
        def queryRangeSum(lower = 0, upper =len(self.nums) - 1, treesIndex = 0):
            nonlocal i,j
            # out of range
            if lower > j or upper < i: return 0
            if i <= lower <= upper <= j: return self.trees[treesIndex]

            middle = lower + int((upper - lower) / 2)
            if middle >= j:
                return queryRangeSum( lower, middle, treesIndex * 2 + 1)
            if middle < i:
                return queryRangeSum( middle + 1, upper, treesIndex * 2 + 2)

            return queryRangeSum( lower, middle, treesIndex * 2 + 1) + queryRangeSum( middle + 1, upper, treesIndex * 2 + 2)
        return queryRangeSum()

# Your NumArray object will be instantiated and called as such:
s = NumArray([1,3,5])
print(s.trees)
print(s.sumRange(0,2))
s.update(1,2)
print(s.sumRange(0,2))
