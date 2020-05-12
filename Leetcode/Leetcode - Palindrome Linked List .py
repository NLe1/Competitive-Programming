"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        #find the middle reference
        slow,fast = head,head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        if fast: slow= slow.next
        def reverse(node):
            if not node.next: return node, node
            ret, newRoot = reverse(node.next)
            node.next = None
            ret.next = node
            return node, newRoot
        firstCur, (_, secondCur) = head, reverse(slow)

        while secondCur:
            if firstCur.val != secondCur.val: return False
            firstCur, secondCur = firstCur.next, secondCur.next
        return True

head = ListNode(1)
s = Solution()
print(s.isPalindrome(head))