# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return None
        stack = []
        ans = []
        ans.append(root.val)
        for item in list(reversed(root.children)):
            stack.append(item)
        while len(stack) > 0:
            item = stack.pop()
            ans.append(item.val)
            for item in list(reversed(item.children)):
                stack.append(item)

        return ans

