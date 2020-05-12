"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        returnHead = ListNode(float('-inf'))
        cur, buffer, cursor, distinct= returnHead, head.val, head.next, True
        while cursor:
            if buffer != cursor.val:
                if not distinct:
                    distinct = True
                else:
                    cur.next = ListNode(buffer)
                    cur = cur.next
                buffer = cursor.val
            else:
                distinct = False
            cursor = cursor.next
        if distinct: cur.next = ListNode(buffer)
        return returnHead.next


s = Solution()
root = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4)))))
s.deleteDuplicates(root)
