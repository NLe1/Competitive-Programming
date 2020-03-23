class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def robSub(self, root) -> [int, int]:
        if not root: return [0,0]
        else:
            left = self.robSub(root.left)
            right = self.robSub(root.right)
            ans = [0,0]
            ans[0] = root.val + left[1] + right[1]
            ans[1] = max(left) + max(right)
            return ans

    def rob(self, root):
        return max(self.robSub(root))
root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
s = Solution()

print(s.rob(root))