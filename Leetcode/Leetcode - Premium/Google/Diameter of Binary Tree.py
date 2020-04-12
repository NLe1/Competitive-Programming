"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.count = float("-inf")
        def helper(root):
            if not root: return -1
            curChain = 0
            countLeft = helper(root.left)
            countRight = helper(root.right)
            if countLeft >= 0: curChain += countLeft + 1
            if countRight >= 0: curChain += countRight + 1
            self.count = max(self.count, curChain)
            return 1 + max(countLeft, countRight)
        helper(root)
        return self.count