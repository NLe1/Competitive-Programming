# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def getLeaves(self, root, leaves1):
        if root.left is None and root.right is None:
            if leaves1:
                self.leaves1.append(root.val)
            else:
                self.leaves2.append(root.val)
            return
        if root.left is not None:
            self.getLeaves(root.left, leaves1)
        if root.right is not None:
            self.getLeaves(root.right, leaves1)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leaves1, self.leaves2 = [], []
        self.getLeaves(root1, True)
        self.getLeaves(root2, False)
        # print(self.leaves1)
        # print(self.leaves2)
        return self.leaves1 == self.leaves2
root1 = TreeNode(1,TreeNode(1), None)
root2 = TreeNode(1, TreeNode(1))
s = Solution()
print(s.leafSimilar(root1, root2))