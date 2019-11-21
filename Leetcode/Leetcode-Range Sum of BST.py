class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def traverse(self, root, n,L,R):
        if root and L <= root.val <= R:
            n+=root.val
        if root.left:
            self.traverse(root.left,n,L,R)
        if root.right:
            self.traverse(root.right,n,L,R)

    def rangeSumBST(self,root, L: int, R: int) -> int:
        n = 0
        self.traverse(root, n)
        return n



