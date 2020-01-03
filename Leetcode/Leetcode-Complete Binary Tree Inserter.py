from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def traverseAndAdd(self, root):
        if not root: return
        q = deque()
        q.appendleft(root)
        while len(q) > 0:
            cur = q.pop()
            self.insert(cur.val)
            if cur.left: q.appendleft(cur.left)
            if cur.right: q.appendLeft(cur.right)

    def __init__(self, root: TreeNode):
        self.count = 0
        self.root = None
        self.traverseAndAdd(root)

    def insert(self, v: int) -> int:
        if self.count == 0:
            self.root = TreeNode(v)
            self.count += 1
        else:
            nCount = self.count + 1
            arr = []
            while nCount != 1:
                arr.append(nCount)
                nCount = int(nCount / 2)
            arr = arr[::-1]
            cur = self.root
            for i, elem in enumerate(arr) :
                if i == len(arr) - 1:
                    if elem %2:
                        cur.right = TreeNode(v)
                    else:
                        cur.left = TreeNode(v)
                else:
                    if elem %2:
                        cur = cur.right
                    else:
                        cur = cur.left
            self.count+=1

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()