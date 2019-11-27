# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res

s = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)),TreeNode(4)),TreeNode(6, None,TreeNode(8, TreeNode(7), TreeNode(9))))
s.increasingBST(root)