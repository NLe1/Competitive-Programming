"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        ans, d = [], collections.defaultdict(int)
        def traverse(node, level):
            if not node: return
            d[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        traverse(root, 0)
        for level, numbers in d.items():
            if level % 2 == 1:
                ans.append(numbers[::-1])
            else:
                ans.append(numbers)
        return ans

