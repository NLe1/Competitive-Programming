# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def helper(self, root1, root2):
        if root1 and not root2 or not root1 and root2:
            return False
        if not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        l = []
        if not root: return True
        return self.helper(root, root)


s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))
print(s.isSymmetric(root))
