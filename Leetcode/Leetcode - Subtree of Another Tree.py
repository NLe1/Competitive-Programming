"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: return False
        if not t: return True
        def inorder(node):
            if not node: return "#"
            return ''.join(["*", str(node.val), inorder(node.left), inorder(node.right)])
        return inorder(t) in inorder(s)


so = Solution()
s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
t = TreeNode(4, TreeNode(1), TreeNode(2))
print(so.isSubtree(s, t))