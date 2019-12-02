# import sys
# sys.setrecursionlimit(10**6)
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def helper(self, grid, startI, endI, startJ, endJ):
        if startI == endI or startJ == endJ:
            return Node(grid[startI][startJ], True, None, None, None, None)
        tl = self.helper(grid, startI, startI + int((endI - startI) / 2), startJ,
                         startJ + int((endJ - startJ) / 2))
        tr = self.helper(grid, startI, startI + int((endI - startI) / 2),
                         startJ + int((endJ - startJ) / 2) + 1, endJ)
        bl = self.helper(grid, startI + int((endI - startI) / 2) + 1, endI, startJ,
                         startJ + int((endJ - startJ) / 2))
        br = self.helper(grid, startI + int((endI - startI) / 2) + 1, endI,
                         startJ + int((endJ - startJ) / 2) + 1,
                         endJ)
        if tl.isLeaf and bl.isLeaf and tr.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            return Node(tl.val, True, None, None, None, None)
        return Node('*', False, tl, tr, bl, br)

    def construct(self, grid) -> Node:
        N = len(grid)
        root = self.helper(grid, 0, N - 1, 0, N - 1)
        return root


grid = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0]
]
s = Solution()
print(s.construct(grid))
