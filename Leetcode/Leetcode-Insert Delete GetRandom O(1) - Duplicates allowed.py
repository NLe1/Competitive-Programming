import random
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        if val not in self.pos:
            self.pos[val] = [len(self.nums)-1]
            print(self.nums)
            print(self.pos)
            return True
        else:
            self.pos[val].append(len(self.nums)-1)
            print(self.nums)
            print(self.pos)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.pos:
            return False
        #index of the last val
        newInd = self.pos[val][-1]
        #val at the end of nums
        last = self.nums[-1]
        #update the new position of the var last
        self.pos[last][self.pos[last].index(len(self.nums)-1)] = newInd
        self.nums[newInd] = last
        if len(self.pos[val]) > 1:
            self.pos[val].pop()
        else:
            del self.pos[val]
        self.nums.pop()
        print(self.nums)
        print(self.pos)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randint(0, len(self.nums)-1)]

# Your RandomizedCollection object will be instantiated and called as such:
s = RandomizedCollection()
print(s.insert(1))
print(s.insert(1))
print(s.insert(2))
print(s.insert(2))
print(s.insert(2))
print(s.remove(1))
print(s.remove(1))
print(s.remove(2))
print(s.insert(1))
print(s.insert(2))

print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())

# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()