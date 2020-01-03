# Definition for a binary tree node.
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse(self, root, d, level):
        if not root: return
        d[level].append(root.val)
        if root.left:
            self.traverse(root.left, d, level + 1)
        if root.right:
            self.traverse(root.right, d, level + 1)

    def levelOrder(self, root: TreeNode):
        if not root: return []
        d = defaultdict(list)
        self.traverse(root, d, 0)
        ans = []
        for key in sorted(d.keys()):
            ans.append(d[key])
        return ans
