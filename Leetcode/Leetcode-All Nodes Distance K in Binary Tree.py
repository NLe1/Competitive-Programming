from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def traverse(self, d,cur, ans, visited,left):
        if left==0 and not visited[cur]:
            visited[cur] = True
            ans.append(cur)
        elif left:
            visited[cur] = True
            for neighbor in d[cur]:
                if not visited[neighbor]:
                    self.traverse(d,neighbor, ans, visited, left-1)

    def helper(self, root, d):
        if not root:
            return
        if root.left:
            d[root.left.val].append(root.val)
            d[root.val].append(root.left.val)
            self.helper(root.left, d)
        if root.right:
            d[root.right.val].append(root.val)
            d[root.val].append(root.right.val)
            self.helper(root.right, d)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        d = defaultdict(list)
        self.helper(root, d)
        ans = []
        visited = {}
        for vertex in d.keys():
            visited[vertex] = False
        self.traverse(d,target.val, ans, visited, K)
        return ans


root = TreeNode(8, TreeNode(7, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6))),
                TreeNode(9, TreeNode(10, None, TreeNode(11)), TreeNode(13, TreeNode(12), TreeNode(14))))
s = Solution()
print(s.distanceK(root, TreeNode(4), 5))
