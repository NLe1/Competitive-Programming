import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, flag, level, d):
        d[level].append(root.val)
        if not flag:
            if root.left:
                self.helper(root.left, not flag, level + 1, d)
            if root.right:
                self.helper(root.right, not flag, level + 1, d)
        else:
            if root.right:
                self.helper(root.right, not flag, level + 1, d)
            if root.left:
                self.helper(root.left, not flag, level + 1, d)

    def zigzagLevelOrder(self, root: TreeNode):
        if not root: return []
        d = collections.defaultdict()
        self.helper(root, True, 0, d)
        return d.values()