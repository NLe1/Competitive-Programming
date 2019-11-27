from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def traverse(self, x, y, root, d):
        if root.left:
            self.traverse(x - 1, y - 1, root.left, d)
        if root.right:
            self.traverse(x + 1, y - 1, root.right, d)
        d[x][y].append(root.val)

    def verticalTraversal(self, root: TreeNode):
        d = defaultdict(lambda: defaultdict(list))
        self.traverse(0, 0, root, d)
        ans = []
        for x in sorted(d.keys()):
            temp = []
            for y in sorted(d[x].keys(), reverse=True):
                for item in sorted(d[x][y]):
                    temp.append(item)
            ans.append(temp)
        return ans


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
s = Solution()
print(s.verticalTraversal(root))
