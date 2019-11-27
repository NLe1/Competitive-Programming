# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        s = [(root, [root.val])]
        ans = 0
        while len(s) > 0:
            node, totals = s.pop()
            ans += totals.count(sum)
            if node.left:
                s.append((node.left, [node.val+x for x in totals]+[node.val]))
            if node.right:
                s.append((node.right, [node.val+x for x in totals]+[node.val]))
        return ans


root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))
s = Solution()
print(s.pathSum(root, 3))
