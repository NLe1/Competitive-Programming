from collections import defaultdict


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums, self.nDict, self.min = [], defaultdict(int), []

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.nDict[x] += 1
        if len(self.min) == 0:
            self.min.append(x)
        else:
            if x < self.min[-1]:
                self.min.append(x)

    def pop(self) -> None:
        if self.nums[-1] == self.min[-1] and self.nDict[self.min[-1]] == 1:
            del self.nDict[self.min[-1]]
            self.min.pop()
        else:
            self.nDict[self.nums[-1]] -= 1
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())
s.pop()
print(s.top())
print(s.getMin())
