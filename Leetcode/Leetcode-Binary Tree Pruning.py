# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left =None , right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: TreeNode):
        if not root: return False
        l,r = self.helper(root.left), self.helper(root.right)
        if not l: root.left = None
        if not r: root.right = None
        return any([l,r,(root.val == 1)])

    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root

root = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(0)), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1)))
s =Solution()
ans = s.pruneTree(root)
print(ans)