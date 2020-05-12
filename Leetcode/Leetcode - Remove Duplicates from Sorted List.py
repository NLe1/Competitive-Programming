"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        iter, cur, prev = head.next, head, head
        while iter:
            if iter.val != prev.val:
                prev = iter
                cur.next = iter
                cur= cur.next
            iter=iter.next
        cur.next = None
        return head

node = ListNode(1, ListNode(1, ListNode(2)))
s = Solution()
print(s.deleteDuplicates(node))