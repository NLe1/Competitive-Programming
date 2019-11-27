import bisect
from collections import defaultdict

class MyCalendarTwo:
    def __init__(self):
        self.d = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        if len(self.d) == 0:
            self.d[(start, end)] = 1
            return True
        l = sorted(self.d.keys(), key=lambda x: x[1])
        # print(l)
        starts, ends = [x[0] for x in l], [x[1] for x in l]
        i, j = bisect.bisect_right(ends, start), bisect.bisect_left(starts, end)
        # print(i,j)
        # print(starts)
        # print(ends)
        if i >= j:
            self.d[(start, end)] = 1
            return True
        for k in range(i, j):
            if self.d[l[k]] >= 2:
                return False
        for k in range(i, j):
            s, e = l[k]
            a = self.d[l[k]]
            if start <= s < end <= e:
                self.d[(s, end)] = a + 1
                if start < s:
                    self.d[(start, s)] = a
                if end < e:
                    self.d[(end, e)] = a
            elif s <= start < e <= end:
                self.d[(start, e)] = a + 1
                if s < start:
                    self.d[(s, start)] = a
                if e < end:
                    self.d[(e, end)] = a
            elif s <= start < end <= e:
                self.d[(start, end)] = a + 1
                if s < start:
                    self.d[(s, start)] = a
                if end < e:
                    self.d[(end, e)] = a
            elif start < s < e < end:
                self.d[l[k]] = a + 1
                self.d[(start, s)] = a
                self.d[(e, end)] = a
            if e != end and s != start:
                del self.d[l[k]]
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
items = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
expect = [True, True, True, True, False, False, True, False, False, False, False, True, True, False, True, False, False,
          True, True, False, True, False, False, False, True, False, False, False, False, False]
for i, (l, r) in enumerate(items):
    # print(f"Adding: ({l}_{r})")
    print(obj.book(l, r), " ", expect[i])
    # print(dict(obj.d))
