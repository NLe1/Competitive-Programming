# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new = None
        ptr1 = l1
        ptr2 = l2

        if not ptr1:
            return ptr2
        if not ptr2:
            return ptr1

        if ptr1 and ptr1.val <= ptr2.val:
            new = ListNode(ptr1.val)
            ptr1 = ptr1.next
        else:
            new = ListNode(ptr2.val)
            ptr2 = ptr2.next

        cur = new
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                cur.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                cur.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            cur = cur.next

        if ptr1 and not ptr2:
            cur.next = ptr1
        else:
            cur.next = ptr2

        return new