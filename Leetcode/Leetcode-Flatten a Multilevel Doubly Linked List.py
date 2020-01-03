# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def helper(self,head):
        cur = head
        while cur.next:
            while cur.next and not cur.child:
                cur = cur.next
            if cur.child:
                tail = self.helper(cur.child)
                tail.next = cur.next
                if cur.next:
                    cur.next.prev = tail
                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
        return cur

    def flatten(self, head):
        if not head: return None
        self.helper(head)
        return head


