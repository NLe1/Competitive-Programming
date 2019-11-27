# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        q, nVal = [root],[]
        while len(q) >0:
            t = q.pop(0)
            nVal.append(t.val)
            if t.left: q.append(t.left)
            if t.right: q.append(t.right)
        nVal.sort()
        min = 100000000000
        for i in range(len(nVal) - 1):
            if abs(nVal[i] - nVal[i+1]) < min:
                min = abs(nVal[i] - nVal[i+1])
        return min
