# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None , right = None):
        self.val = x
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.s = set()
        q = [(root, 0)]
        self.s.add(0)
        while len(q) > 0:
            t,v = q.pop()
            if t.left:
                q.append((t.left, v * 2 + 1))
                self.s.add(v * 2 + 1)
            if t.right:
                q.append((t.right, v * 2 + 2))
                self.s.add(v * 2 + 2)
        print(self.s)

    def find(self, target: int) -> bool:
        return target in self.s

# Your FindElements object will be instantiated and called as such:
root = TreeNode(-1, TreeNode(-1), TreeNode(-1,TreeNode(-1), TreeNode(-1, TreeNode(-1))))
obj = FindElements(root)

