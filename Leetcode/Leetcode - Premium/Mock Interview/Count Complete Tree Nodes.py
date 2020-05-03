"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        # node, x position, y position
        stack = [(root, 0, 0)]
        record = collections.defaultdict(list)
        while stack:
            cur,x,y = stack.pop()
            if not cur.left or not cur.right: record[y].append(x)
            if cur.left: stack.append((cur.left, x - 1 ,y + 1))
            if cur.right: stack.append((cur.right, x + 1, y + 1))
        maxHeight = max(record.keys())
        if maxHeight == 0: return 1
        totalLeavesBottom = len(record[maxHeight])
        return 2**(maxHeight) + totalLeavesBottom - 1