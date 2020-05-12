"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def helper(root1,root2):
            if not root1 and not root2: return None
            if root1 and root2:
                newRoot = TreeNode(root1.val + root2.val)
                newRoot.left = helper(root1.left, root2.left)
                newRoot.right = helper(root1.right, root2.right)
            else:
                if root1:
                    newRoot = TreeNode(root1.val)
                    newRoot.left = helper(root1.left, None)
                    newRoot.right = helper(root1.right, None)
                else:
                    newRoot = TreeNode(root2.val)
                    newRoot.left = helper(root2.left, None)
                    newRoot.right = helper(root2.right, None)
            return newRoot
        return helper(t1,t2)

