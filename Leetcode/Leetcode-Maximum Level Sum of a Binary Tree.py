# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, level):
        self.d[level] = level if level not in self.d else self.d[level] + root.val
        if root.left: self.helper(root.left, level+1)
        if root.right: self.helper(root.right, level+1)

    def maxLevelSum(self, root: TreeNode) -> int:
        self.d = dict()
        self.helper(root, 1)
        return  self.d.values().index(max(self.d.values)) + 1