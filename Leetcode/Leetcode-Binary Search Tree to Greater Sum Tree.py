# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def preOrderGet(self, root: TreeNode, l):
        if root is None: return
        self.preOrderGet(root.left,l)
        l.append(root.val)
        self.preOrderGet(root.right,l)

    def preOrderSet(self, root: TreeNode, l):
        if root is None: return
        self.preOrderSet(root.left,l)
        root.val = sum(l[self.c:])
        self.c+=1
        self.preOrderSet(root.right,l)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        l=[]
        self.preOrderGet(root, l)
        self.c=0
        self.preOrderSet(root, l)
        return root

s = Solution()
r = TreeNode(4,TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6,TreeNode(5), TreeNode(7,None,TreeNode(8))))
s.bstToGst(r)
print()