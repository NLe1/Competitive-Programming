from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def  __init__(self):
        self.d = defaultdict(list)

    def helper(self, root: TreeNode, depth: int, pos: int):
        if root is None: return
        self.d[depth].append(pos)
        self.helper(root.left, depth + 1, pos * 2 + 1)
        self.helper(root.right, depth + 1, pos * 2 + 2)

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root, 0, 0)
        ma = 1
        for c, v in self.d.items():
            v.sort()
            if len(v) > 1:
                m = v[-1] - v[0] + 1
                if m > ma:
                    ma = m
        return ma


s = Solution()
r = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)))
print(s.widthOfBinaryTree(r))
print()
