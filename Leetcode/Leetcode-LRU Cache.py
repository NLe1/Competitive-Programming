class LRUCache:
    def __init__(self, MSize):
        self.size = MSize
        self.cache = {}
        self.next, self.before = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.before[b] = b, a

    def delete(self, key):
        self.connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key]

    def append(self, k, v):
        self.cache[k] = v
        self.connect(k, self.next[self.head])
        self.connect(self.head, k)
        if len(self.cache) > self.size:
            self.delete(self.before[self.tail])

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache: self.delete(key)
        self.append(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

c = LRUCache(2)
c.put(1,1)
c.put(2,2)
print(c.get(1))
c.put(3,3)
print(c.get(2))

