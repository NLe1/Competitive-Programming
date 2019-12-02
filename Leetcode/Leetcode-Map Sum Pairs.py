from bisect import bisect_left, bisect_right
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
    def sum(self, prefix: str) -> int:
        l = list(self.d.keys())
        l.sort()
        ind = bisect_left(l, prefix)
        sum = 0
        while ind < len(l):
            k = l[ind]
            if k.startswith(prefix):
                sum+=self.d[k]
            else:
                break
            ind+=1
        return sum

# Your MapSum object will be instantiated and called as such:
s = MapSum()
s.insert("apple", 3)
print(s.sum("ap"))
s.insert("app", 2)
print(s.sum("ap"))
