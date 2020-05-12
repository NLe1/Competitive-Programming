"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ Recursively """
        # def helper(left, right):
        #     if not left and not right: return True
        #     if left and right:
        #         return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        #     else: return False
        # return helper(root.left, root.right)

        """ Iteratively """
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else: return False
        return True
