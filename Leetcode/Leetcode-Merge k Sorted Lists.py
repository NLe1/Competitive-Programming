import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        d, head, cur = collections.defaultdict(list), None, None
        for node in lists: d[node.val].append(node)
        while len(d) > 0:
            curMin = sorted(d.keys())[0]
            curList = d[curMin]
            curNode = curList.pop()
            if len(curList) == 0:
                del d[curMin]
            if curNode.next:
                d[curNode.next.val].append(curNode.next)
            if not head: head = curNode
            if cur:
                cur.next = curNode
            cur = curNode

        return head