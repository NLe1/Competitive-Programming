"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(local):
            if not local: return 0
            nonlocal ans
            left = max(helper(local.left), 0)
            right = max(helper(local.right), 0)
            includeRoot = local.val + left + right
            ans = max(ans, includeRoot)
            return local.val + max(left,right)
        ans = float('-inf')
        helper(root)
        return ans

s = Solution()
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.maxPathSum(root))