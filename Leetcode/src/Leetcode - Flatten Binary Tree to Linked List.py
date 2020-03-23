import collections

class Solution:
    def helper(self, root, queue):
        if not root: return
        queue.append(root)
        self.helper(root.left, queue)
        self.helper(root.right, queue)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        q = collections.deque
        self.helper(root, q)
        root = q.popleft()
        cur = root
        while len(q):
            next = q.popleft()
            cur.left = None
            cur.right= next
            cur = next
        return root

