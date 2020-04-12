"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2 if l2 else None
        if not l2: return l1 if l1 else None
        ret = cur = None
        carry = 0
        while l1 and l2:
            curNum = l1.val + l2.val + carry
            if not ret:
                ret = ListNode(curNum % 10)
                cur = ret
                carry = int(curNum / 10)
            else:
                cur.next = ListNode(curNum % 10)
                carry = int(curNum / 10)
                cur=cur.next
            l1=l1.next
            l2=l2.next
        while l1:
            curNum = l1.val + carry
            cur.next = ListNode(curNum % 10)
            carry = int(curNum / 10)
            cur = cur.next
            l1=l1.next

        while l2:
            curNum = l2.val + carry
            cur.next = ListNode(curNum % 10)
            carry = int(curNum / 10)
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)

        return ret

l1 = ListNode(1, ListNode(8))
l2 = ListNode(0)
s = Solution()
ret = s.addTwoNumbers(l1, l2)
while ret:
    print(ret.val)
    ret = ret.next