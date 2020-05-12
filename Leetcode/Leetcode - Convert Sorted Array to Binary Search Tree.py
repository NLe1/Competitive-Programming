"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        def helper( lower, upper):
            nonlocal nums
            if lower > upper: return None
            if lower == upper: return TreeNode(nums[lower])
            middle = lower + int((upper - lower)/ 2)
            rootNode = TreeNode(nums[middle])
            rootNode.left = helper(lower, middle - 1)
            rootNode.right = helper(middle + 1, upper)
            return rootNode
        ans =  helper(0, len(nums) - 1)
        return ans

s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))