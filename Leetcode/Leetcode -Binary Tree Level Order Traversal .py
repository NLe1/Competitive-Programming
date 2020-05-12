"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        q = collections.deque([(root, 0)])
        while stack:
            node,level = q.popleft()
            d[level].append(node.val)
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))
        return d.values()