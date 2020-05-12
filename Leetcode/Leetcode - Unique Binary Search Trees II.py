"""

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        def helper(lower, higher):
            if lower == higher: return [TreeNode(lower)]

            ans = []
            for i in range(lower, higher + 1):
                if i == lower:
                    for node in helper(lower + 1, higher):
                        newRoot = TreeNode(i)
                        newRoot.right= node
                        ans.append(newRoot)
                elif i == higher:
                    for node in helper(lower, higher - 1):
                        newRoot = TreeNode(i)
                        newRoot.left = node
                        ans.append(newRoot)
                else:
                    for leftNode in helper(lower, i - 1):
                        for rightNode in helper(i + 1, higher):
                            newRoot = TreeNode(i)
                            newRoot.left = leftNode
                            newRoot.right = rightNode
                            ans.append(newRoot)
            return ans
        return helper(1, n)

s = Solution()
print(s.generateTrees(4))