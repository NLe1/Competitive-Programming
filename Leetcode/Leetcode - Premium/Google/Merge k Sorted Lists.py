"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

# Definition for singly-linked list.
from heapq import heapify, heappush, heappop, heapreplace
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next
lists = [ListNode(5, ListNode(8, ListNode(10))), ListNode(4, ListNode(12)), ListNode(3, ListNode(4, ListNode(6)))]
s = Solution()
node = s.mergeKLists(lists)
while node:
    print(node.val)
    node = node.next