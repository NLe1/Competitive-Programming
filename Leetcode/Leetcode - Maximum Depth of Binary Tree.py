"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return
        m = 0
        def helper(node, level):
            nonlocal m
            if not node: return
            #leaf node
            if not node.left and not node.right:
                m =max(m,level)
                return
            else:
                helper(node.left,level + 1)
                helper(node.right,level + 1)
        return helper(node, 1)

s = Solution()
print(s.maxDepth())