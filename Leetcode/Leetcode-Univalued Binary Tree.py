# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self,root: TreeNode, pVal: int):
        if not root: return True
        return root.val == pVal and self.helper(root.left, root.val) and self.helper(root.right, root.val)
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.helper(root.left, root.val) and self.helper(root.right, root.val)

