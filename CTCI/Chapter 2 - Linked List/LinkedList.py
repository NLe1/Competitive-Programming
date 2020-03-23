class Node:
    def __init__(self, value = 0):
        self.next = None
        self.data = value

class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = self.tail = None

    def append(self,  value):
        if self.head == None and self.tail == None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.count+=1

    def insert(self, value, index):
        if self.count < index < 0:
            return
        else:
            newNode = Node(value)
            #append to head
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            #append to tail
            elif index == self.count:
                self.append(value)
            else:
                prev = self.get(index - 1)
                newNode.next = prev.next
                prev.next = newNode
            self.count+=1

    #delete node that has value @param(value)
    def deleteNode(self, value):
        prev, cur = None, self.head
        while cur != None:
            if cur.data == value:
                break
            prev = cur
            cur = cur.next
        if cur == None:
            return
        else:
            self.count -= 1
            prev.next = cur.next

        return cur

    #get node at index in the linkedlist
    def get(self, index):
        #validate input
        assert 0 <= index <= self.count
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur



