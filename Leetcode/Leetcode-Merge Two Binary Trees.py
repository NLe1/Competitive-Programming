# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode, t3=None) -> TreeNode:
        if t1 and t2:
            t3 = TreeNode(t1.val + t2.val)
            if t1.left or t2.left:
                t3.left = self.mergeTrees(t1.left, t2.left)
            if t1.right or t2.right:
                t3.right = self.mergeTrees(t1.right, t2.right)
        else:
            if t1:
                t3 = TreeNode(t1.val)
                t3.left =self.mergeTrees(t1.left, None)
                t3.right=self.mergeTrees(t1.right, None)
            elif t2:
                t3 = TreeNode(t2.val)
                t3.left =self.mergeTrees(None, t2.left)
                t3.right=self.mergeTrees(None, t2.right)
        return t3

left = TreeNode(1,TreeNode(3,TreeNode(5)),TreeNode(2))
right= TreeNode(2,TreeNode(1, None, TreeNode(4)), TreeNode(3,None,TreeNode(7)))

s = Solution()
print(s.mergeTrees(left,right))
