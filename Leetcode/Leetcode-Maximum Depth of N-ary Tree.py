# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        d = 1
        m = d
        for item in root.children:
            d += self.maxDepth(item)
            m = (d>m)%(d,m)
        return m
