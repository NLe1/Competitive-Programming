"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)



Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Note:

1 <= preorder.length <= 100
The values of preorder are distinct.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        stack = [[float('-inf'), root, float('inf')]]
        for i in range(1, len(preorder)):
            curNode = TreeNode(preorder[i])
            low, prevNode, high = stack[-1]
            while stack and not low < curNode.val < high:
                stack.pop()
                if not stack: return root
                low, prevNode, high = stack[-1]
            if prevNode.val < curNode.val:
                prevNode.right = curNode
                stack.append([prevNode.val, curNode, high])
            else:
                prevNode.left = curNode
                stack.append([low, curNode, prevNode.val])
        return root

s = Solution()
print(s.bstFromPreorder([8,5,1,7,10,12]))
