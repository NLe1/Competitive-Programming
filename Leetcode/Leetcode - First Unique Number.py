"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]

Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
"""

class Node:
    def __init__(self, val):
        # self.prev = prev
        # self.next = next
        self.val = val

class FirstUnique:

    def connect(self, node1, node2):
        self.pre[node2] = node1
        self.post[node1] = node2

    def getNode(self,val):
        return self.nodes[val]

    def delete(self, val):
        curNode = self.getNode(val)
        prev, next = self.pre[curNode], self.post[curNode]
        self.connect(prev, next)

    def enqueue(self, node):
        self.connect(self.pre[self.tail], node)
        self.connect(node, self.tail)

    def dequeue(self, node):
        if self.count == 0: return
        self.delete(self.post[self.head])

    def __init__(self, nums: [int]):
        self.head, self.tail = Node("+"), Node("-")
        self.nodes, self.pre, self.post = dict(), dict(), dict()
        self.connect(head,tail)
        self.seen = set()
        self.count = 0
        for num in nums:
            if num not in self.seen:
                self.seen.add(num)
                self.nodes[num] = Node(num)
                self.count+=1
                self.enqueue(self.nodes[num])


    def showFirstUnique(self) -> int:
        if self.count > 0: return self.post[self.head].val
        else: return -1

    def add(self, value: int) -> None:
        if value not in self.seen:
            self.count +=1
            self.nodes[value] = Node(value)
            self.enqueue(self.nodes[value])

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)