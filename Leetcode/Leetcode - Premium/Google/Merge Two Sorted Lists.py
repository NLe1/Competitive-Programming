"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        cur1, cur2 = l1, l2
        head = cur = None
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                if not head:
                    head = cur = ListNode(cur1.val)
                else:
                    cur.next = ListNode(cur1.val)
                    cur=cur.next
                cur1=cur1.next
            else:
                if not head:
                    head = cur = ListNode(cur2.val)
                else:
                    cur.next = ListNode(cur2.val)
                    cur=cur.next
                cur2=cur2.next
        if cur1: cur.next = cur1
        if cur2: cur.next = cur2
        return head

s = Solution()
s1 = ListNode(1, ListNode(2, ListNode(4)))
s2 = ListNode(1, ListNode(3, ListNode(6)))
s = s.mergeTwoLists(s1, s2)
while s:
    print(s.val)
    s = s.next
