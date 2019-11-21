# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return None
        q = []
        ans = []
        q.append(root)
        while len(q) > 0:
            temp = q.pop()
            ans.append(temp.val)
            q.extend(temp.children)

        return list(reversed(ans))