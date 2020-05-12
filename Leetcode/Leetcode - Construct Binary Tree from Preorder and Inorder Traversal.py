"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder: return None
        indexes = dict()
        for i, num in enumerate(inorder):
            indexes[num] = i
        root = TreeNode(preorder[0])
        stack = [root]
        cur = 1
        while cur < len(preorder) and stack:
            num = preorder[cur]
            newNode = TreeNode(num)
            numIndex = indexes[num]
            if numIndex < indexes[stack[-1].val]:
                stack[-1].left = newNode
                stack.append(newNode)
            else:
                if numIndex > indexes[root.val]: break
                stack[-1].right = newNode
                stack.append(newNode)
            cur+=1
        stack.append(root)

        while cur < len(preorder) and stack:
            num = preorder[cur]
            newNode = TreeNode(num)
            numIndex = indexes[num]
            if numIndex > indexes[stack[-1].val]:
                stack[-1].right = newNode
                stack.append(newNode)
            else:
                if numIndex < indexes[root.val]: break
                stack[-1].left = newNode
                stack.append(newNode)
            cur += 1
        return root

s = Solution()
print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))