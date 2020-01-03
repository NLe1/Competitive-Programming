
class LRUCache:
    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.limit = capacity
        self.count = 0
        self.head, self.tail = None, None
        self.d = dict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            # update the value
            cur = self.d[key]
            # update the pointer if only it is not head node
            if cur == self.tail:
                cur.prev.next = None
                self.tail = cur.prev
                cur.prev = None
                cur.next = self.head
                self.head.prev = cur
                self.head = cur
            elif cur != self.head:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.prev = None
                cur.next = self.head
                self.head.prev = cur
                self.head = cur
            return cur.val


    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            self.count += 1
            # Create a new node
            newNode = self.Node(key, value)
            # make the node become the head Node
            if self.head:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.d[key] = newNode
            else:
                self.head = newNode
                self.tail = newNode

            self.d[key]= newNode

            # check for overflow
            if self.count > self.limit:
                temp = self.tail
                temp.prev.next = None
                self.tail = temp.prev
                temp.prev = None
                self.count -= 1
                #delete out of the dict
                del self.d[temp.key]
        else:
            #update the value
            cur = self.d[key]
            cur.val = value

            #update the pointer if only it is not head node
            if cur.prev:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.prev = None
                cur.next = self.head
                self.head.prev = cur
                self.head = cur
"""

import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.limit = capacity
        self.count = 0
        self.d = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            val = self.d[key]
            del self.d[key]
            self.d[key] =val
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value
        else:
            self.d[key] = value
            self.count+=1
            #if overflow, delete the first element
            if self.count > self.limit:
                del self.d[list(self.d.keys())[0]]
"""



# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))