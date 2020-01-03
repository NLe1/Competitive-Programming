# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, lower = float('-inf'), upper = float('inf')) -> bool:
        if not root: return True
        left,right = True,True
        if root.left:
            if not lower < root.left < root.val:
                left = False
            else:
                left = self.isValidBST(root.left, lower, root.val)
        if root.right:
            if not root.val < root.right< upper:
                left = False
            else:
                right = self.isValidBST(root.right, root.val, upper)
        return left and right

