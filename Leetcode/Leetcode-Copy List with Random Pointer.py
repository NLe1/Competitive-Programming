# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        d = dict()
        d[head] = Node(head.val)
        d[None] = None
        prev = head
        cur = head.next
        while cur:
            d[cur] = Node(cur.val)
            d[prev].next = d[cur]
            prev, cur = cur, cur.next

        cur = head
        while cur:
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
