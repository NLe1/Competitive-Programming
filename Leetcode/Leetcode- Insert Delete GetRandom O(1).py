import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.s:
            self.s[val] = 0
            return True
        return False
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.s:
            return False
        else:
            del self.s[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        s = list(self.s.keys())
        return s[random.randint(0, len(s)-1)]

# Your RandomizedSet object will be instantiated and called as such:
s = RandomizedSet()
print(s.insert(1))
print(s.remove(1))
print(s.insert(0))
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())


# param_1 =obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()